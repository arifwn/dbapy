from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash

from app import db
from app.users.decorators import requires_login

mod = Blueprint('dbapy', __name__)

@mod.route('/')
@requires_login
def home():
    return render_template("dbapy/index.html")
