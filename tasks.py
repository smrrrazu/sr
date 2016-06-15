# -*- coding: utf-8 -*-
from invoke import task, run

print("Inside tasks.py")

@task
def install():
    '''Creates a virtual environment and installs required packages.'''

    # Apache HTTP Server (development headers) (prerequisite for mod_wsgi package)
    run('apt-get install -y apache2-dev')

    # Install Python WSGI adapter module for Apache
    run('apt-get install -y libapache2-mod-wsgi-py3')

    # Interface to the GNU readline library (prerequisite for 'readline' package)
    run('apt-get install -y libncurses5-dev')

    # Install Redis server
    # run('apt-get install -y redis-server')

    # Create an empty sr database
    run('mysql -e "CREATE DATABASE IF NOT EXISTS sr CHARACTER SET utf8 COLLATE utf8_unicode_ci"')

    # Install, create and activate virtual environment
    print("Installing virtualen")
    run("pwd")
    run('pip3 install virtualenv')
    # run('pip install --upgrade virtualenv')
    run('virtualenv --always-copy venv')

    # Activate virtual env and install required Python packages
    # Needs to to be run together since each run() is a separate process

    run('. venv/bin/activate && pip install -r requirements.txt')

    # Clean up after installing all Ubuntu packages
    run('apt-get autoremove')

    # Collect static
    # run('. venv/bin/activate && ./manage.py collectstatic --noinput')

    # Migrate database schema
    run('. venv/bin/activate && cd /var/www/domains/sr/sr')
    run('python manage.py migrate')

    run('python manage.py runserver 0.0.0.0:8000')
