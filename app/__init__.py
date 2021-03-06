from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

from app.users.sessions import UserSessionInterface

app = Flask(__name__)
app.config.from_object('config')
app.session_interface = UserSessionInterface()

db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def not_found(error):
    return render_template('500.html'), 500


from app.users.views import mod as usersModule
app.register_blueprint(usersModule)

from app.dbapy.views import mod as dbapyModule
app.register_blueprint(dbapyModule)