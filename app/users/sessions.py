
import pickle
from datetime import timedelta
from uuid import uuid4

from werkzeug.datastructures import CallbackDict
from flask.sessions import SessionInterface, SessionMixin


class UserSession(CallbackDict, SessionMixin):

    def __init__(self, initial=None, sid=None, new=False):
        def on_update(self):
            self.modified = True
        CallbackDict.__init__(self, initial, on_update)
        self.sid = sid
        self.new = new
        self.modified = False


class UserSessionInterface(SessionInterface):
    serializer = pickle
    session_class = UserSession

    def __init__(self):
        pass

    def generate_sid(self):
        return str(uuid4())

    def open_session(self, app, request):
        from app.users.models import Session
        
        sid = request.cookies.get(app.session_cookie_name)
        if not sid:
            sid = self.generate_sid()
            return self.session_class(sid=sid, new=True)

        s = Session.query.filter_by(session_id=sid).first()

        if s:
            data = self.serializer.loads(s.data)
            return self.session_class(data, sid=sid)
        return self.session_class(sid=sid, new=True)

    def save_session(self, app, session, response):
        from app.users.models import Session
        from app import db

        domain = self.get_cookie_domain(app)
        if not session:
            s = Session.query.filter_by(session_id=session.sid).first()
            if s:
                db.session.delete(s)
                db.session.commit()

            if session.modified:
                response.delete_cookie(app.session_cookie_name,
                                       domain=domain)
            return

        s = Session.query.filter_by(session_id=session.sid).first()
        if not s:
            s = Session(session_id=session.sid)
            db.session.add(s)

        s.data = self.serializer.dumps(dict(session))
        db.session.commit()

        response.set_cookie(app.session_cookie_name, session.sid,
                            expires=s.expired, httponly=True,
                            domain=domain)
