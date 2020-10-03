#encoding:utf-8
#app/routes/rt_excelmap.py

from bottle import Bottle,route,template,request,static_file
from app.utils.excelmap import excelmapping

excelmap = Bottle()

@excelmap.route('/')
def excelmapIndex(subapp='excelmap',num=2):
    return template('excelmap')

@excelmap.route('/upload',method='POST')
def excelmap_upload():
    upload0 = request.files.get('data0')
    upload1 = request.files.get('data1')
    field = request.forms.get('field')
    mod = request.forms.get('mod')#merge()函数的how参数

    #print(field)
    field = field.strip().replace(' ','')

    if upload0 == None or upload1 == None:
        return "缺少文档"
    if field == None:
        return "缺少匹配字段"

    import os.path
    name0,ext0 = os.path.splitext(upload0.filename)
    name1,ext1 = os.path.splitext(upload1.filename)
    if ext0.lower() not in ('.xls','.xlsx'):
        return name0,ext0,"文件格式不正确,上传xls,xlsx格式文件"
    if ext1.lower() not in ('.xls','.xlsx'):
        return name1, ext1, "文件格式不正确,上传xls,xlsx格式文件"

    savePath = './temp/' #相对于项目根目录
    filename0 = savePath + upload0.filename
    filename1 = savePath + upload1.filename
    if not os.path.exists(savePath):
        os.mkdir(savePath)
    upload0.save(filename0,overwrite=True)
    upload1.save(filename1,overwrite=True)

    result = excelmapping(filename0,filename1,field,savePath,mod)
    fname = os.path.basename(result)#从路径中截取文件名部分
    return static_file(fname,root=savePath,download=True)

