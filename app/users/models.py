
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
        return '<User %r: %r>' % (self.name, self.email)

    @classmethod
    def create_user(cls, name, email, password, is_admin=False):
        from app import db

        user = cls(name=name, email=email, password=generate_password_hash(password), is_admin=is_admin)
        db.session.add(user)
        db.session.commit()

        return user
