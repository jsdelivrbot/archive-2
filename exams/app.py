#!/usr/bin/env python3

from bottle import Bottle, route, run, template, static_file
from helper import Helper

import os, sys
dirname = os.path.dirname(sys.argv[0])


app=Bottle()

myHelper = Helper()

@app.route('/')
def index():
  return template('index', math_content=myHelper.Content)

run(app, reloader=True, host='localhost', port=8080, debug=True)
