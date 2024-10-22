"""
WSGI config for usefsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'usefsite.settings')

application = get_wsgi_application()
[program:gunicorn]

directory=/home/ubuntu/Portofolio_Website

command=/home/ubuntu/Portofolio_Website/venv/bin/gunicorn --workers 3 --bind unix:/home/ubuntu/Portofolio_Website/app.sock usefsite.wsgi:application  

autostart=true

autorestart=true

stderr_logfile=/var/log/gunicorn/gunicorn.err.log

stdout_logfile=/var/log/gunicorn/gunicorn.out.log



[group:guni]

programs:gunicorn


Sample django.conf: