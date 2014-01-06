#!/usr/bin/env python

import os
import readline
from pprint import pprint

from flask import *
from app import *

os.environ['PYTHONINSPECT'] = 'True'

try:
    import bpython
    bpython.embed(locals())
    exit()
except ImportError:
    pass
