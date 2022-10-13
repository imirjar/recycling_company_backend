# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u0941681/data/www/vtormet-resurs.ru/vtormetresurs')
sys.path.insert(1, '/var/www/u0941681/data/vtormet_env/lib/python3.9/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'vtormetresurs.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
