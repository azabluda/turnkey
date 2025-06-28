#!/bin/sh
# Start Gunicorn (Flask API) in the background
cd /app/backend && gunicorn -b 127.0.0.1:8000 main:app &
# Start Nginx in the foreground
nginx -g 'daemon off;'
