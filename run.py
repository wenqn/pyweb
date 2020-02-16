# encoding:utf-8

from bottle import run,TEMPLATE_PATH
TEMPLATE_PATH.append("./app/templates/")
from app.routes import *




if __name__ == '__main__':
    app.run(port=8080,reloader=True,debug=True)