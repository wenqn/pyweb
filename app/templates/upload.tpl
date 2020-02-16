% if subapp == 'root':
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" size="100" name="data"  value="浏览">
        <input type="submit" name="submit" value="上传" >
    </form>
% else:
    <form action="{{subapp}}/upload" method="post" enctype="multipart/form-data">
        <input type="file" size="100" name="data"  value="浏览">
        <input type="submit" name="submit" value="上传" >
    </form>
%end