
import datetime

from werkzeug import check_password_hash, generate_password_hash

from app import db

class User(db.Model):
    __tablename__ = 'users_user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    is_admin = db.Column(db.Boolean())
    password = db.Column(db.String(255))

    def __init__(self, name=None, email=None, password=None, is_admin=False):
        self.name = name
        self.email = email
        self.password = password
        self.is_admin = is_admin

    def __repr__(self):
        return '<user %r: %r>' % (self.name, self.email)

    @classmethod
    def create_user(cls, name, email, password, is_admin=False):
        from app import db

        user = cls(name=name, email=email, password=generate_password_hash(password), is_admin=is_admin)
        db.session.add(user)
        db.session.commit()

        return user


class Session(db.Model):
    __tablename__ = 'users_session'
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(255), unique=True)
    data = db.Column(db.LargeBinary())
    expired = db.Column(db.DateTime())

    def __init__(self, session_id=None, data=None, expired=None):
        self.session_id = session_id
        self.data = data
        self.expired = expired if expired else datetime.datetime.now() + datetime.timedelta(days=30)

    def __repr__(self):
        return '<session %r>' % (self.session_id)

    @classmethod
    def clear(cls):
        for session in cls.query.all():
            db.session.delete(session)
        db.session.commit()

    @classmethod
    def clear_expired(cls):
        now = datetime.datetime.now()
        for session in cls.query.all():
            if now > session.expired:
                db.session.delete(session)
        db.session.commit()
