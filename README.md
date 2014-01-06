DBApy
=====

Online Database Administration Tool


What is this?
=============

DBApy is a web-based database administration tools. BDApy is written in Python and uses Flask microframework and Bootstrap.


Features
========

- Easy to use, responsive web-based GUI.
- Quick one-liner setup for local database.
- Secure online mode, with multifactor authentication support (using Google Authenticator)


Supported Database
==================

DBApy currently supports PostgreSQL. Support for MySQL/MariaDB is planned in the future.


Installation
============

```
./shell.py
>>> from app import db
>>> db.create_all()
```
