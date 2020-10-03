<!-- 上传单个文件 -->
% if subapp == 'root':
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" size="100" name="data"  value="浏览">
        <input type="submit" name="submit" value="上传" >
    </form>
% else:
    <form action="/{{subapp}}/upload" method="post" enctype="multipart/form-data">
        <input type="file" size="100" name="data"  value="浏览">
        % # 用户可以自定义line，template（）函数中，如果line被定义，则嵌入line，否则pass
        % if 'line' in dir():
            {{!line}}
        % end
        <input type="submit" name="submit" value="上传" >
    </form>
% end