#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import Bottle, run, template, static_file, request, redirect
from beaker.middleware import SessionMiddleware
from database import db
import datetime

app = Bottle()

@app.route('/:filename#.*#')
def send_static(filename):
    return static_file(filename, root='./static')

@app.route('/', method='GET')
def home():
  logged = request.params.logged
  usuarios = []
  mensaje = ''
  if logged == 'true':
    mensaje = 'Ususario logeado'
    proyecion = {'_id': 1, 'usuario': 1}
    usuarios_collection = db['usuarios'].find({}, proyecion)
    for d in usuarios_collection:
      usuarios.append(d)
  locals = {
    'title': 'Bienvenido',
    'mensaje': mensaje,
    'usuarios': usuarios
  }
  return template('home/index', locals)

@app.route('/login', method='GET')
def login():
  locals = {
    'title': 'Acceso al Sistema',
    'mensaje': ''
  }
  return template('login/index', locals)

@app.route('/login/sign_up', method='GET')
def sign_up():
  locals = {
    'title': 'Crear cuenta',
    'mensaje': ''
  }
  return template('login/sign_up', locals)

@app.route('/login/sign_up', method='POST')
def create_account():
  # pametros
  usuario = request.params.usuario
  contrasenia = request.params.contrasenia
  contrasenia2 = request.params.contrasenia2
  if contrasenia != contrasenia2:
    locals = {
      'title': 'Crear cuenta',
      'mensaje': 'Contraseñas no coinciden'
    }
    return template('login/sign_up', locals)
  else:
    document = {'usuario': usuario, 'contrasenia': contrasenia, 'accesos': []}
    collection_usuarios = db['usuarios'] 
    collection_usuarios.insert_one(document)
    redirect('/login')

@app.route('/login', method='POST')
def login_acceder():
  # pametros
  usuario = request.params.usuario
  contrasenia = request.params.contrasenia
  query = {'usuario': usuario, 'contrasenia': contrasenia}
  collection_usuarios = db['usuarios'] 
  documents = collection_usuarios.find(query)
  # acceso de db
  n = 0
  for d in documents:
    n = n + 1
    # agregar loging a documento
    momento = datetime.datetime.now()
    collection_usuarios.update_one(
      query, {
        '$push': { 
          'accesos': momento
          }
        }, upsert = True
    )
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
  run(app_session, host='0.0.0.0', port=8081, debug=True, reloader=True)