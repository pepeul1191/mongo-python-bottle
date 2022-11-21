% include('_header.tpl')
<h1>Bienvenido</h1>
{{mensaje}}<br>
<form action="/login" method="post">
  <label for="name">Usuario:</label><br>
  <input type="text" id="usuario" name="usuario">
  <br>
  <label for="name">Contraseña:</label><br>
  <input type="password" id="contrasenia" name="contrasenia">
  <br><br>
  <button class="btn">Ingresar</button>
</form>
<br>
<a href="/">Ir al Inicio</a>
<a href="/login/sign_up">Crear Cuenta</a>
% include('_footer.tpl')