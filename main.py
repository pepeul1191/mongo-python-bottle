#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import Bottle, run, template, static_file, request, redirect
from beaker.middleware import SessionMiddleware
#from database import engine

app = Bottle()

@app.route('/:filename#.*#')
def send_static(filename):
    return static_file(filename, root='./static')

@app.route('/', method='GET')
def home():
  session = request.environ.get('beaker.session')
  locals = {
    'title': 'Bienvenido',
  }
  if session != None:
    if session['logged']:
      return template('home/index')
  return redirect('/login')

@app.route('/login', method='GET')
def login():
  session = request.environ.get('beaker.session')
  locals = {
    'title': 'login',
  }
  if session != None:
    if session['logged']:
      return redirect('/')
  return template('login/index')

if __name__ == '__main__':
  app_session = SessionMiddleware(
    app, 
    {
      'session.type': 'file',
      'session.cookie_expires': 6000,
      'session.data_dir': './data',
      'session.auto': True
    }
  )
  run(app, host='0.0.0.0', port=8081, debug=True, reloader=True)