<!-- 上传多个文件 -->
% if subapp == 'root':
    % try:
        % # 用户可以自定义title，template（）函数中，如果title被定义，则嵌入title，否则pass
        % if title:
            {{!title}}
        % end
    % except NameError:
        % pass
    % end

    <form action="/upload" method="post" enctype="multipart/form-data">
        % for i in range(num):
            <input type="file" size="100" name="data{{i}}"  value="浏览">
        % end

        % # 用户可以自定义line，template（）函数中，如果line被定义，则嵌入line，否则pass
        % if 'line' in dir():
            {{!line}}
        % end
        <input type="submit" name="submit" value="上传" >
    </form>

% else:
   % # 用户可以自定义title，template（）函数中，如果title被定义，则嵌入title，否则pass
   % if title:
       {{!title}}
   % end

    <form action="/{{subapp}}/upload" method="post" enctype="multipart/form-data">
        % for i in range(num):
            <input type="file" size="100" name="data{{i}}"  value="浏览"><br />
        % end

        % # 用户可以自定义line，template（）函数中，如果line被定义，则嵌入line，否则pass
        % if 'line' in dir():
            {{!line}}
        % end

        <input type="submit" name="submit" value="上传" >
    </form>
%end