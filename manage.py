#!/usr/bin/env python
import os
import sys
import glob


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")

    """
    Two things are wrong with Django's default `SECRET_KEY` system:

    1. It is not random but pseudo-random
    2. It saves and displays the SECRET_KEY in `settings.py`

    This snippet
    1. uses `SystemRandom()` instead to generate a random key
    2. saves the SECRET_KEY file in the `envdir` directory

    The result is a random and safely hidden `SECRET_KEY`.
    """
    PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
    SECRET_FILE = os.path.join(PROJECT_PATH, 'envdir', 'SECRET_KEY')
    try:
        SECRET_KEY = open(SECRET_FILE).read().strip()
    except IOError:
        try:
            import random
            SECRET_KEY = ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
            secret = file(SECRET_FILE, 'w')
            secret.write(SECRET_KEY)
            secret.close()
        except IOError:
            Exception('Please create a %s file with random characters \
            to generate your secret key!' % SECRET_FILE)

    if 'test' in sys.argv:
        env_dir = os.path.join('tests', 'envdir')
    else:
        env_dir = 'envdir'
    env_vars = glob.glob(os.path.join(env_dir, '*'))
    for env_var in env_vars:
        with open(env_var, 'r') as env_var_file:
            os.environ.setdefault(env_var.split(os.sep)[-1],
                                  env_var_file.read().strip())

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
