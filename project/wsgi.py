import sys
import os


PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.abspath(PROJECT_DIR + '/../'))

activate_this = PROJECT_DIR + '/../venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from django.core.handlers.wsgi import WSGIHandler

os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
application = WSGIHandler()
