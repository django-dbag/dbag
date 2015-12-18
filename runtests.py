#!/usr/bin/env python

import sys

from django.conf import settings
from django.core.management import execute_from_command_line

if not settings.configured:
    settings.configure(
        DATABASE_ENGINE='sqlite3',
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
            },
        },
        INSTALLED_APPS=[
            'django.contrib.auth',
            'django.contrib.admin',
            'django.contrib.sessions',
            'django.contrib.contenttypes',

            'dbag',

            'tests',
        ],
        ROOT_URLCONF='',
        DEBUG=False,
        TEMPLATE_DEBUG=True,
        TEMPLATE_STRING_IF_INVALID="INVALID_TEMPLATE_VARIABLE",
    )


def runtests():
    argv = sys.argv[:1] + ['test', 'tests', '--traceback'] + sys.argv[1:]  # noqa
    execute_from_command_line(argv)

if __name__ == '__main__':
    runtests()
