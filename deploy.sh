#!/bin/bash

cd /home/ubuntu/MyWebsite
git pull origin main

# Activate the virtual environment
source /home/ubuntu/env/bin/activate

# Install any new dependencies
pip install -r requirements.txt

# Apply migrations if necessary
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Restart Gunicorn using Supervisor
sudo supervisorctl restart gunicorn

# Restart Nginx
sudo systemctl restart nginx
