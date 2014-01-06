

from app import db


class Server(db.Model):
    __tablename__ = 'dbapy_postgresql_server'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    address = db.Column(db.String(255)) # tcp:localhost:5432, ssl:localhost:5432; unix:/var/postgres
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    databases = db.relationship('Database', backref='server', lazy='dynamic')
    roles = db.relationship('Role', backref='server', lazy='dynamic')

    def __init__(self, name=None, address=None, username=None, password=None):
        self.name = name
        self.address = address
        self.username = username
        self.password = password

    def __repr__(self):
        return '<server %r>' % (self.name,)

    def reload(self):
        # reload cache: delete all database objects associated with this server
        pass


class Database(db.Model):
    __tablename__ = 'dbapy_postgresql_database'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    server_id = db.Column(db.Integer, db.ForeignKey('server.id'))
    tables = db.relationship('Table', backref='database', lazy='dynamic')

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<database %r>' % (self.name,)

    def reload(self):
        # reload cache: delete all table objects associated with this database
        pass



class Table(db.Model):
    __tablename__ = 'dbapy_postgresql_table'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    database_id = db.Column(db.Integer, db.ForeignKey('database.id'))
    columns = db.relationship('Column', backref='table', lazy='dynamic')

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<table %r>' % (self.name,)

    def reload(self):
        # reload cache: delete all column objects associated with this table
        pass


class Column(db.Model):
    __tablename__ = 'dbapy_postgresql_column'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    field_type = db.Column(db.String(255))
    table_id = db.Column(db.Integer, db.ForeignKey('table.id'))

    def __init__(self, name=None, field_type=None):
        self.name = name
        self.field_type = field_type

    def __repr__(self):
        return '<column %r>' % (self.name,)

    def reload(self):
        pass


class Role(db.Model):
    __tablename__ = 'dbapy_postgresql_role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    server_id = db.Column(db.Integer, db.ForeignKey('server.id'))

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<role %r>' % (self.name,)

    def reload(self):
        pass


class Constrain(object):
    pass

