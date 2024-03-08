"""
WSGI config for first_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

# This file is a simple gateway between the web server and the Django application.
# It is used to help the web server communicate with the Django application.


import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'robot_controller.settings')

application = get_wsgi_application()
