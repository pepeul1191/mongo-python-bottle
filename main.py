#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import Bottle, run, template, static_file, request, redirect
from beaker.middleware import SessionMiddleware
from bson.objectid import ObjectId
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

@app.route('/usuario/editar', method='GET')
def detalle_usuario_editar():
    # pametros
    usuario_id = request.params.id
    # acceso de db
    usuarios_collection = db['usuarios']
    query = {'_id': ObjectId(usuario_id)}
    usuario = usuarios_collection.find_one(query)
    # devolver datos a una vista
    locals = {'usuario': usuario, 'titulo': 'Editar Usuario', 'title': 'Editar Usuario'}
    return template('usuario/detail', locals)
  
@app.route('/usuario/eliminar', method='GET')
def usuario_eliminar():
    # pametros
    usuario_id = request.params.id
    # acceso de db
    usuarios_collection = db['usuarios']
    query = {'_id': ObjectId(usuario_id)}
    usuarios_collection.find_one_and_delete(query)
    # devolver datos a una vista
    redirect('/')

@app.route('/usuario/editar', method='POST')
def usuario_editar():
  # pametros
    usuario_id = request.params.id
    usuario = request.params.usuario
    contrasenia = request.params.contrasenia
    # acceso de db
    usuarios_collection = db['usuarios']
    query = {'_id': ObjectId(usuario_id)}
    document = {'usuario': usuario, 'contrasenia': contrasenia}
    usuario = usuarios_collection.find_one_and_update(query, {'$set': document})
    # devolver datos a una vist
    redirect('/')

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