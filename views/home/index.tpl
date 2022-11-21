% include('_header.tpl')
<h1>home</h1>
% if mensaje == '':
<a href="/login">Ingresar al Sistema</a>
% else:
<label>{{mensaje}}</label>
% end
% include('_footer.tpl')