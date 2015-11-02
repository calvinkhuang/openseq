"""
WSGI config for openseq project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import sys, os
INTERP = "/home/openseq/opensequencer.com/env/bin/python"
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

cwd = os.getcwd()
sys.path.append(cwd)
sys.path.append(cwd + '/openseq')

sys.path.insert(0, cwd + '/env/bin')
sys.path.insert(0, cwd + '/env/lib/python2.7/site-packages/django')
sys.path.insert(0, cwd + '/env/lib/python2.7/site-packages')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "openseq.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
