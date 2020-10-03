#bottle apache adapter
#不依赖run.py文件
import sys,os

sys.path = ['/var/www/pyweb/'] + sys.path
path=os.chdir(os.path.dirname(__file__))

#must import bottle after setup sys.path
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append('./app/templates')
from app.routes import *   
from app.routes.__init__ import app

application = app

