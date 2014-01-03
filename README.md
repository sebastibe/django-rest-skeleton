Django REST Skeleton
====================

**A Django REST framework project template for quickly bootstraping REST APIs**

---

This is an opinionated [Django][django] project skeleton based on:

* [Django REST framework][django-rest-framework]
* Environment Variable and database urls based settings
* Migrations with [South][south]
* Deployment with [fabric][fabric]
* Documentation with [Sphinx][sphinx]
* Cache with [Redis][redis]

---

Installation
------------

After installing Django, You can install the project template with
`django-admin.py`:

    django-admin.py startproject --template=https://github.com/sebastibe/django-rest-skeleton/archive/master.zip myproject

Settings
--------

Set your settings values within the envdir folder in development or
production. To set `Debug = True` for example:

    $ echo "true" > envdir/DEBUG

We also use heroku-like database urls:

    $ echo "postgres://postgres@localhost:5432/project" > envdir/DATABASE_URL

Database
--------

Setup [PostgreSQL][postgresql], preferably by running the commands as a
`postgres` user with `sudo -u postgres`:

    $ createuser -d -A -P username
    $ createdb -O username dbname

No need of `-d` option when creating database in production.

Install and run [Redis][redis]:

    $ redis-server


Project layout
--------------

    my_project
        ...
        hosting          <- deployment configuration files
            staging      <- templates for 'staging' server
                nginx.config
                supervisord.config
                ...
            production
                ...
        reqs             <- project's pip requirement files
            all.txt      <- main requirements file, list all requirements
            deploy.txt   <- deployment related dependencies
            testing.txt  <- requirements for testing
            apps.txt     <- external django apps
            docs.txt     <- requirements for documentation
            django.txt   <- direct django related packages
            database.txt <- database related dependencies
            ...
        api   <- REST API source directory
            settings.py  <- settings
            ...
        docs             <- Sphinx_ documentation > make html
        manage.py
        fabfile.py       <- project's Fabric deployment script
            ...

Tests
-----

Tests are autodiscovered within the `/tests` folder. You can run them all with:

    $ python manage.py test

Or if you can run only the tests in a specific module with:

    $ python manage.py test full.dotted.path.to.test_module


Documentation
-------------

In the `/docs` folder, run the Sphinx helper:

    $ sphinx-quickstart

For documenting your Django code, be sure to to say yes to the "autodoc"
extension. You can take a look at the [following gist][sphinx-conf-gist]
to enable Django models discovery.

Deployment
----------

Use [daemontools]'s envdir program to manage application secrets
(SECRET_KEY, DATABASE_URL, SENTRY_DSN, etc.).

Use a process watcher such as [supervisord] or [circus] to run the web
server. Example:

    command=envdir /path/to/envdir /path/to/env/bin/gunicorn api.wsgi:application -k gevent -b 127.0.0.1:8000 -w 2


License
-------

Copyright (c) 2013, Sébastien Béal
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this
list of conditions and the following disclaimer in the documentation and/or
other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

[django]: https://www.djangoproject.com/
[django-rest-framework]: http://django-rest-framework.org/
[south]: http://south.aeracode.org/
[fabric]: http://fabfile.org/
[sphinx]: http://sphinx.pocoo.org/
[sphinx-conf-gist]: http://gist.github.com/sebastibe/4450508
[supervisord]: http://supervisord.org/
[markdown]: http://pypi.python.org/pypi/Markdown/
[postgresql]: http://www.postgresql.org/
[redis]: http://redis.io/
[daemontools]: http://cr.yp.to/daemontools.html
[circus]: http://circus.readthedocs.org/
