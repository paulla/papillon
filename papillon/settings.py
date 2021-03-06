#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Django settings for papillon project.
# Don't edit this file. Put your changes in local_settings.py

DEBUG = False
TEMPLATE_DEBUG = DEBUG

import os
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

EXTRA_URL = 'papillon/'

TINYMCE_URL = 'http://localhost/tinymce/'
MAX_COMMENT_NB = 10 # max number of comments by poll - 0 to disable comments
ALLOW_FRONTPAGE_POLL = False # disabled is recommanded for public instance
# time to live in days
DAYS_TO_LIVE = 30

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': PROJECT_PATH + '/papillon.db',   # Or path to database file if using sqlite3.
        'USER': '',                     # Not used with sqlite3.
        'PASSWORD': '',                         # Not used with sqlite3.
        'HOST': '',                             # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                             # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://www.postgresql.org/docs/8.1/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
# although not all variations may be possible on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Paris'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'fr-fr'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = PROJECT_PATH + '/static/'

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
# if you have set an EXTRA_URL set the full path
MEDIA_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
# if you have set an EXTRA_URL set the full path
ADMIN_MEDIA_PREFIX = '/static/admin/'

SECRET_KEY = ''

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

ROOT_URLCONF = 'papillon.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_PATH + '/templates',
)

INSTALLED_APPS = (
    # contribs
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.markup',

    # third parties
    'south',

    # app
    'papillon.polls',
)

LANGUAGES = (
  ('fr', 'Français'),
  ('en', 'English'),
)

try:
    from local_settings import *
except ImportError, e:
    print 'Unable to load local_settings.py:', e
