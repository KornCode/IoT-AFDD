#!/bin/sh
# set -e

echo "🚀 Starting Django development server with polling autoreload..."

python manage.py runserver 0.0.0.0:5005
