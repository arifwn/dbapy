from functools import wraps

from flask import g, flash, redirect, url_for, request

import config


def requires_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if (getattr(g, 'user', None) is None) and getattr(config, 'SECURE_ACCESS', False):
            flash(u'You need to be signed in for this page.', 'danger')
            return redirect(url_for('users.login', next=request.path))
        return f(*args, **kwargs)
    return decorated_function


def requires_admin(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if (getattr(g, 'user', None) is None) and getattr(config, 'SECURE_ACCESS', False):
            flash(u'You need to be signed in for this page.', 'danger')
            return redirect(url_for('users.login', next=request.path))
        elif getattr(g, 'user', None) and (not getattr(g, 'user', None).is_admin) and getattr(config, 'SECURE_ACCESS', False):
            flash(u'You need to be signed in as an administrator for this page.', 'danger')
            return redirect(url_for('users.login', next=request.path))
        return f(*args, **kwargs)
    return decorated_function
