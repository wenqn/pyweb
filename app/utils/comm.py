import os.path

# checkExt()
# uploadlist:[request.files对象列表]
# extlist:扩展名元组或列表
def checkExt(uploadlist,extlist):
    #import os.path
    for each in uploadlist:
        if not each:
            return "请上传文档"
        name, ext = os.path.splitext(each.filename)
        if ext.lower() not in extlist:
            return name, ext, "文件格式不正确，请上传", extlist, "格式的文件"
    return True

# savefile()
# upload:request.files对象
# fpath:'./path/',路径最后带'/'
def savefile(fpath, upload):
    #import os.path
    savef = fpath + upload.filename

    if not os.path.exists(fpath):
        os.mkdir(fpath)

    upload.save(savef, overwrite=True)
    return savef

# subname（）
# filepath:含有路径的文件名
# filename：去掉路径的文件名
def subname(filepath):
    filename = os.path.basename(filepath)
    return filename

# list_tohtml(lst)
# lst:列表
def list_tohtml(lst):
    print('<table>')
    for i in lst:
        print('<tr><td>')
        print(i)
        print('</td></tr>')
    print('<tr><td>长度：' + str(len(lst)) + '</td></tr>')
    print('</table>')

