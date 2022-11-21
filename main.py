#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import Bottle, run, template, static_file, request, redirect
from beaker.middleware import SessionMiddleware
from database import db

app = Bottle()

@app.route('/:filename#.*#')
def send_static(filename):
    return static_file(filename, root='./static')

@app.route('/', method='GET')
def home():
  logged = request.params.logged
  mensaje = ''
  if logged == 'true':
    mensaje = 'Ususario logeado'
  locals = {
    'title': 'Bienvenido',
    'mensaje': mensaje
  }
  return template('home/index', locals)

@app.route('/login', method='GET')
def login():
  locals = {
    'title': 'Acceso al Sistema',
    'mensaje': ''
  }
  return template('login/index', locals)

@app.route('/login', method='POST')
def login_acceder():
  # pametros
  usuario = request.params.usuario
  contrasenia = request.params.contrasenia
  query = {'usuario': usuario, 'contrasenia': contrasenia}
  rs = db['usuarios'].find(query)
  # acceso de db
  n = 0
  for d in rs:
    n = n + 1
  # devolver datos a una vista
  if n == 1:
    return redirect('/?logged=true')
  else:
    locals = {
      'title': 'Acceso al Sistema',
      'mensaje': 'Usuario y/o contraseña no válidos'
    }
    return template('login/index', locals)

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