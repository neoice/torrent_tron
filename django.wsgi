#!/usr/bin/env python
import sys, os

sys.path.append('/srv/torrent_tron')
sys.path.append('/srv/torrent_tron/rtorrent_interface')

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
