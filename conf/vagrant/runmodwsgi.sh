#!/usr/bin/env bash

# Script to start the mod-wsgi server in a dettached screen session
screen -dmS server
screen -S server -X stuff "cd /var/www/domains/sr$(printf \\r)"
screen -S server -X stuff ". venv/bin/activate$(printf \\r)"
screen -S server -X stuff "./manage.py runmodwsgi --reload-on-changes$(printf \\r)"