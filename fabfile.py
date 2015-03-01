from fabric.api import *
from YamJam import yamjam

rpi_ip = yamjam()['rpi']['ip']
rpi_password = yamjam()['rpi']['password']
rpi_home = yamjam()['rpi']['home']
rpi_venv_bin = yamjam()['rpi']['venv_bin']


env.hosts = [rpi_ip]
env.password = rpi_password


def command(command):
    run('{}'.format(command))


def deploy():
    with cd(rpi_home):
        run('git pull')
        run('{}pip install -r requirements/production.txt'.format(rpi_venv_bin))
        run('{}python manage.py makemigrations'.format(rpi_venv_bin))
        run('{}python manage.py migrate'.format(rpi_venv_bin))
        restart_server()


def install(package):
    sudo('apt-get install {}'.format(package))


def restart_server():
        sudo('supervisorctl restart all')


def upgrade():
    sudo('apt-get update')
    sudo('apt-get dist-upgrade')
