# encoding:utf-8
# app/routes/rt_ziming.py

from app.utils.zmtoexcel import zmto_csv
from bottle import Bottle, route, template, request


ziming = Bottle()


@ziming.route('/')
def zm_upload(subapp=None):
    return template('upload',subapp='ziming')


@ziming.route("/upload",method="POST")
def zm_doupload(downfile=None):
    upload = request.files.get("data")
    import os.path
    name, ext = os.path.splitext(upload.filename)
    print(name)
    if ext not in (".txt",".TXT"):
        return "文件类型错误,请上传txt格式文件"

    csvf = zmto_csv(upload.file)
    print(csvf.name)
    return template('download',downfile=csvf)

