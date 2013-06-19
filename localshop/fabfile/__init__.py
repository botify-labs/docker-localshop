import os

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
    # Evaluate the contextual localshop.rc variables
    # and push them to environment.
    # Fetch the user, pass and mail from system env,
    # assuming docker build has set them already
    local("/bin/bash -c 'source localshop.rc'")
    localshop_user = os.environ['LOCALSHOP_USER']
    localshop_pass = os.environ['LOCALSHOP_PASSWORD']
    localshop_mail = os.environ['LOCALSHOP_MAIL']
    
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
