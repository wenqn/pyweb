# enconding:utf-8
# app/routes/__init__.py

from bottle import route, Bottle, template, request
from app.routes.rt_ziming import ziming

app = Bottle()


@app.route('/login')
def login():
    return '<p>hello login</p>'


@app.route('/logout')
def logout():
    return '<p>hello logout</p>'


@app.route('/index')
def upload(subapp=None):
    return template('upload',subapp='root')


@app.route('/upload', method='POST')
def do_upload():
    upload = request.files.getunicode('data')
    import os.path
    name, ext = os.path.splitext(upload.filename)
    return name, ext


# 自明排课表
app.mount("/ziming", ziming)
