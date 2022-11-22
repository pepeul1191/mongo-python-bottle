% include('_header.tpl')
<h1>{{titulo}}</h1>
<form action="/usuario/editar" method="post">
  <input type="hidden" name="id" value="{{usuario['_id']}}"><br>
  <label for="name">Usuario:</label><br>
  <input type="text" id="usuario" name="usuario" value="{{usuario['usuario']}}"><br>
  <label for="name">Contraseña:</label><br>
  <input type="password" id="contrasenia" name="contrasenia" value="{{usuario['contrasenia']}}"><br>
  <br><br>
  <button class="btn">Guardar Cambios</button><br><br>
  Accesos:
  <table>
  <thead>
    <th>Momento</th>
  </thead>
  <tbody>
    % for d in usuario['accesos']:
    <tr>
      <td>{{d}}</td>
    </tr>
    % end
  </tbody>
</table>
</form>
% include('_footer.tpl')