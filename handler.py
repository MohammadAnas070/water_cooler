from django.core.handlers.wsgi import WSGIHandler
from django.core.wsgi import get_wsgi_application

# Ensure Django settings are configured
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'watercooler.settings')  # Replace with your actual Django settings module

# Create a WSGI application object
application = WSGIHandler()
