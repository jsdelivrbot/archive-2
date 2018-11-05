#!/usr/bin/env python3

from bottle import Bottle, route, run, template, static_file
from helper import Helper

import os, sys
dirname = os.path.dirname(sys.argv[0])

myHelper = Helper()

app=Bottle()

@app.route('/')
def index():
  return template('index', chapters=myHelper.Content)

@app.route('/static/css/<filename:re:.*\.css>')
def send_css(filename):
  return static_file(filename, root=dirname + '/static/css')


@app.route('/static/js/<filename:re:.*\.js>')
def send_js(filename):
  return static_file(filename, root=dirname + '/static/js')

@app.route('/static/img/<chapter:re:[1-9]\d*>/<page:re:[1-9]\d*\.jpg>')
def send_img(chapter, page):
  return static_file(str(page), root=dirname + '/static/img/' + str(chapter))
  
run(app, host='localhost', port=8080, debug=True)
