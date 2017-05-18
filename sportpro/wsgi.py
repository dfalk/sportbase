"""
WSGI config for initpro project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os, sys
sys.path.append('C:/Users/user/Bitnami Django Stack projects/sportpro')
os.environ.setdefault("PYTHON_EGG_CACHE", "C:/Users/user/Bitnami Django Stack projects/sportpro/egg_cache")


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sportpro.settings")

application = get_wsgi_application()
