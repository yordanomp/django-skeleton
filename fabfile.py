from fabric.api import *
from fabric.contrib import console


def staging():
    env.path = '/home/wmendez/project'
    env.hosts = ['wmendez@HOST:22', ]


def production():
    env.path = '/home/wmendez/project'
    env.hosts = ['wmendez@HOST:22', ]



def runserver(cli_args=''):
    local('venv/bin/python project/manage.py runserver 0.0.0.0:8000 %s' % cli_args)


def pushpull():
    local('git push') # runs the command on the local environment
    command = 'cd %(path)s; git pull;' % env
    run(command) # runs the command on the remote environment


def deploy():
    command = 'cd %(path)s; cd project;' % env
    command += '%(path)s/venv/bin/python manage.py compilemessages; ' % env
    if console.confirm("Run migrations?", default=False):
        command += '%(path)s/venv/bin/python manage.py migrate; ' % env
        command += '%(path)s/apache2/bin/restart' % env

    run(command)
