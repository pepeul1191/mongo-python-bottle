% include('_header.tpl')
<h1>{{titulo}}</h1>
<form action="/usuario/editar" method="post">
  <input type="hidden" name="id" value="{{sangre['id']}}"><br>
  <label for="name">Nombres:</label><br>
  <input type="text" id="nombre" name="nombre" value="{{sangre['nombre']}}">
  <br><br>
  <button class="btn">Guardar Cambios</button>
</form>
% include('_footer.tpl')