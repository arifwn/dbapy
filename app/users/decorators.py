from functools import wraps

from flask import g, flash, redirect, url_for, request

import config


def requires_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if (getattr(g, 'user', None) is None) and (getattr(config, 'SECURE_ACCESS', False)):
            flash(u'You need to be signed in for this page.')
            return redirect(url_for('users.login', next=request.path))
        return f(*args, **kwargs)
    return decorated_function
