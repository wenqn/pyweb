<!-- 将列表或字典内容以表格形式列出 -->
% include('header.tpl')
<table>

% if isinstance(obj, list):
    % for i in obj:
         <tr><td>{{i}}</td></tr>
    % end
    <tr><td>长度：{{len(obj)}} </td></tr>
% elif isinstance(obj, dict):
    % for i in obj:
        <tr><td>{{i}}</td><td>{{obj[i]}}</td></tr>
    % end
    <tr><td>长度</td><td>{{len(obj)}}</td></tr>
% end
</table>