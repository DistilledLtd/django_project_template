"""
WSGI config for django_project_template project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

if not os.environ.get('DJANGO_SETTINGS_MODULE'):
  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings")

import newrelic.agent
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
NEW_RELIC_INI = os.path.join(BASE_DIR, 'newrelic.ini')
newrelic.agent.initialize(NEW_RELIC_INI)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
