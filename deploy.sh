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

#!/bin/bash

# Extract unique IPs from access log
LOG_FILE="/var/log/nginx/access.log"
OUTPUT_FILE="/home/ubuntu/scripts/daily_ips_$(date +%F).txt"

# Extract unique IP addresses and save them to the output file
awk '{print $1}' $LOG_FILE | sort | uniq > $OUTPUT_FILE

# Example: Send the log to an email (replace with your email setup)
mail -s "Daily IP Log" ymbusinesses@example.com < $OUTPUT_FILE

# Optional: Clear the access log after extraction
# : > $LOG_FILE
