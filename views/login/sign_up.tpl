% include('_header.tpl')
<h1>Crear Cuenta</h1>
{{mensaje}}<br>
<form action="/login/sign_up" method="post">
  <label for="name">Usuario:</label><br>
  <input type="text" id="usuario" name="usuario">
  <br>
  <label for="name">Contraseña:</label><br>
  <input type="password" id="contrasenia" name="contrasenia">
  <br>
  <label for="name">Repetir Contraseña:</label><br>
  <input type="password" id="contrasenia" name="contrasenia2">
  <br><br>
  <button class="btn">Crear Cuenta</button>
</form>
<br>
<a href="/">Ir al Inicio</a>
<a href="/login">Ingresar al Sistema</a>
% include('_footer.tpl')