import os
import ConfigParser

from fabric.context_managers import prefix
from fabric.api import *

activate_virtualenv = "/bin/bash -c 'source /home/localshop/venv/bin/activate'"


@task
def localshop_install():
    """Installs localshop in preexisting virtualenv"""
    with prefix(activate_virtualenv):
        local("pip install localshop")


@task
def localshop_init():
    """Emulates the localshop init phase"""
    # Extract the user, pass and mail from config file,
    # assuming docker build has set them already
    config = ConfigParser.ConfigParser()
    config.read("localshop.conf")

    localshop_user = config.get('superuser', 'username')
    localshop_pass = config.get('superuser', 'password')
    localshop_mail = config.get('superuser', 'mail')

    # Compute localshop super creation instruction
    # from environement variables
    superuser_create = "from django.contrib.auth.models import User; "\
                       "User.objects.create_superuser('{user}', '{mail}', '{password}')"
    superuser_create = superuser_create.format(
        user=localshop_user,
        mail=localshop_mail,
        password=localshop_pass
    )

    with prefix(activate_virtualenv):
        local("su localshop -c 'localshop syncdb --noinput'")  # Ensure db is created by localshop
        local("localshop migrate")
        local('echo "{inst}" | localshop shell'.format(inst=superuser_create))

