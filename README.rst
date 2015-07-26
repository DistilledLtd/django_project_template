{{ project_name }}
========================================================

Initial Setup
========================================================

:code:`django-admin startproject {{ project_name }} --template=https://github.com/DistilledLtd/django_project_template/archive/master.zip --extension=py,rst,ini`


Pip
~~~~~~~~
:code:`pip install -r requirements.txt`


Opbeat
~~~~~~~~

1) Update :code:`OPBEAT` dictionary in {{project_name}}/settings/production.py and {{project_name}}/settings/staging.py with ORGANIZATION_ID and SECRET_TOKEN
2) Create 2 [new opbeat apps](https://opbeat.com/distilled/new-app/)
    - Choose "Custom" deployment method
    - First new app is Production - copy the APP_ID into {{project_name}}/settings/production.py
    - Second new app is Staging - copy the APP_ID into {{project_name}}/settings/staging.py

New Relic
~~~~~~~~~~~

1) Update the license_key setting in {{ project_name }}/newrelic.ini
2) Ensure the deploy script has NEW_RELIC_ENVIRONMENT set to staging for the staging deploy as per the comment in {{ project_name }}/wsgi.py     

Logging
~~~~~~~~~~~~~~

1) Create /var/log/{{ project_name }}/{{ project_name }}.log and ensure Django has perms to write to it


Allowed Hosts
~~~~~~~~~~~~~~

Add relevant host name to ALLOWED_HOSTS in {{project_name}}/settings/production.py and {{project_name}}/settings/staging.py
