Django REST Skeleton
====================

**A Django REST framework project template for quickly bootstraping APIs**

---

This is an opinionated [Django][django] project skeleton based on:

* [Django REST framework][django-rest-framework]
* Migrations with [South][south]
* Deployment with [fabric][fabric]
* Documentation with [Sphinx][sphinx]

---

Database
--------

Setup [PostgreSQL][postgresql], preferably by running the commands as a
`postgres` user with `sudo -u postgres`:

    $ createuser -D -A -P database-user
    $ createdb -O database-user database-name


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
            settings.py  <- general settings complemented by local, staging...
            dev_settings.py
            prod_settings.py
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