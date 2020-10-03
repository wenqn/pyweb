#encoding utf-8
#/app/routes/rt_quchong.py

from bottle import Bottle, template, request, static_file
from app.utils.quchong import *
from app.utils.comm import *

quchong = Bottle()

@quchong.route('/')
def quchong_index(subapp='quchong'):
    return template('quchong')

@quchong.route('/upload', method='POST')
def quchong_count():
    data = request.files.get('data')
    cnt = request.forms.get('count')
    if data == None:
        return template('nofile', exts=('xls', 'xlsx'))

    checkExt([data], ('xls', 'xlsx'))

    savepath = './temp/'
    exfile = savefile(savepath, data)
    if cnt == 'True':
        result = countcells(exfile)
    else:
        result = rmduplicate(exfile)
    return template('tohtml', obj = result)

