# encoding:utf-8
# app/routes/rt_zongping.py

from bottle import Bottle, template, request, static_file
from app.utils.zongping import *
from app.utils.comm import *

zongping = Bottle()

@zongping.route('/')
def zongpingIndex(subapp='zongping'):
    return template('zongping')

@zongping.route('/download/<filename:path>')
def zongping_download(filename):
    print('ok')
    #from urllib.parse import unquote
    #filename = unquote(filename)
    #filename = filename.encode('utf-8')

    # 绕过网址带中文路径，下载链接用英文名，下载文件被替换成相应中文名称
    rename = {'1-teachers.xlsx': '1-任课安排.xlsx',
              '2-students.xlsx': '2-学生信息.xlsx',
              '3-schedule.xlsx': '3-课表.xlsx',
              '1-upsubject.xls': '课程计划导入模板.xls',
              '2-upcourse.xls': '教学班-选课结果导入模板.xls',
              '3-upschedule.xls': '课程表导入模板.xls'}

    return static_file(filename, root='./app/static/zongping/', download=rename[filename])# root 相对路径以pyweb为根目录

@zongping.route('/upload0', method='POST')
def zongping_upload0():
    data0    = request.files.get('course')
    data1    = request.files.get('student')
    preNo    = request.forms.get('preno')
    preName  = request.forms.get('prename')
    classNum = request.forms.get('classnum')

    if not data0:
        return "请上传任课安排"
    if not data1:
        return "请上传学生信息"
    if not preNo:
        return "请填写教学班号前缀"
    if not preName:
        return "请填写教学班名称前缀"
    if not classNum:
        return "请填写班级数量"

    checkExt([data0, data1], ('.xls', '.xlsx'))

    savepath='./temp/'
    fname0 = savefile(savepath, data0)
    fname1 = savefile(savepath, data1)

    # filename1,filename2含有路径信息
    filename1 = toTechCourse(fname0, savepath, preNo, preName, classNum)
    filename2 = toStCourse(filename1, fname1, savepath)

    # 取文件名，去掉路径
    filename1 = subname(filename1)
    filename2 = subname(filename2)
    return static_file(filename2, root=savepath, download=True)

@zongping.route('/upload1', method='POST')
def zongping_upload1():
    data0 = request.files.get("course1")
    data1 = request.files.get('teacher')
    data2 = request.files.get('schedule')

    if not data0:
        return '请上传 教学班-任课老师-学生选课数据.xlsx'
    if not data1:
        return '请上传 任课安排.xlsx'
    if not data2:
        return '请上传 课表.xlsx'

    checkExt([data0, data1, data2], ('.xls', '.xlsx'))

    savepath = './temp/'
    fname0 = savefile(savepath, data0)
    fname1 = savefile(savepath, data1)
    fname2 = savefile(savepath, data2)

    filename = toClassTimeDate(fname0, fname1, fname2, savepath)
    filename = subname(filename) #去掉路径保留文件名
    return static_file(filename, root=savepath, download=True)

