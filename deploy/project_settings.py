# this is for settings to be used by tasks.py
# this is for settings to be used by tasks.py
from __future__ import unicode_literals, absolute_import

import os
from os import path

###############################
# THESE SETTINGS MUST BE EDITED
###############################

# This is the directory inside the project dev dir that contains the django
# application
project_name = "idsapi"

repo_type = "git"
repository = 'git@github.com:oriel-hub/api.git'

# put "django" here if you want django specific stuff to run
# put "plain" here for a basic apache app
project_type = "django"

# django_dir = "django/" + project_name

# openapi_integration holds all the tests that require a connection to the
# server
django_apps = ['openapi', 'userprofile', 'openapi_integration']


# does this virtualenv for python packages
use_virtualenv = True

# python version - major version must be exact, minor version is the minimum
python_version = (3, 6)

################################
# PATHS TO IMPORTANT DIRECTORIES
################################

# set the deploy directory to be the one containing this file
local_deploy_dir = path.dirname(__file__)

local_vcs_root = path.abspath(path.join(local_deploy_dir, os.pardir))

# the path from the VCS root to the django root dir
relative_django_dir = path.join('django', project_name)
#relative_django_dir = path.join('django', 'website')

# the directory the settings live in, relative to the vcs root
#relative_django_settings_dir = path.join(relative_django_dir, project_name)
relative_django_settings_dir = relative_django_dir

# the path from the VCS root to the virtualenv dir
relative_ve_dir = path.join(relative_django_dir, '.ve')

# requirements can be in a single file, or in a directory
# the requirements file
requirements_per_env = False
local_requirements_file = path.join(local_deploy_dir, 'pip_packages_devel.txt')
use_site_packages = True

# the requirements directory
#requirements_per_env = True
#local_requirements_dir = path.join(local_deploy_dir, 'requirements')
# and the files should be path.join(requirements_dir, '%s.txt' % environment)

test_cmd = ' manage.py test -v0 ' + ' '.join(django_apps)

# django jenkins version - latest might require a too new version of django
#django_jenkins_version = '0.14.0'  # compatible with Django 1.5

# servers, for use by fabric

# production server - if commented out then the production task will abort
host_list = {
    'boorka':       ['boorka.ids.ac.uk'],
    'drooga':       ['drooga.ids.ac.uk'],
    'tacuma':       ['31.221.49.74'],
}

# this is the default git branch to use on each server
default_branch = {
    'boorka':       'idsapi_v2_django_1_11',
    'drooga':       'idsapi_v2_django_1_11',
    'tacuma':       'python3_upgrade',
}

# where on the server the django apps are deployed
server_home = '/var/django'

# the top level directory on the server
# underneath it there will be dev/ containing the live instance
# and previous/ containing old copies for rollback
server_project_home = path.join(server_home, project_name)

# which web server to use (or None)
webserver = 'apache'

import socket

if socket.getfqdn().endswith('.fen.aptivate.org'):
    pypi_cache_url = 'http://fen-vz-pypicache.fen.aptivate.org/simple'

###################################################
# OPTIONAL SETTINGS FOR FABRIC - will be put in env
###################################################

use_sudo = False
python_bin = '/usr/bin/python3.6'

# if you have an ssh key and particular user you need to use
# then uncomment the next 2 lines
#user = "root"
#key_filename = ["/home/shared/keypair.rsa"]
