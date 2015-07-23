"""
WSGI config for django_project_template project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

from django.core.wsgi import get_wsgi_application
import newrelic.agent

# NB in Staging the NEW_RELIC_ENVIRONMENT variable must be set to 'staging'
# in order for it to use the staging settings of the newrelic.ini
newrelic.agent.initialize('/python/{{ project_name }}/newrelic.ini')

application = get_wsgi_application()
