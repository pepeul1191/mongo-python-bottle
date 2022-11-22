% include('_header.tpl')
<h1>home</h1>
% if mensaje == '':
<a href="/login">Ingresar al Sistema</a>
% else:
<label>{{mensaje}}</label>
<br><br>
<table>
  <thead>
    <th>Usuario</th>
    <th>Acciones</th>
  </thead>
  <tbody>
    % for d in usuarios:
    <tr>
      <td>{{d['usuario']}}</td>
      <td>
        <a href="/usuario/editar?id={{d['_id']}}">Editar</a>
        <a href="/usuario/eliminar?id={{d['_id']}}">Eliminar</a>
      </td>
    </tr>
    % end
  </tbody>
</table>
% end
% include('_footer.tpl')