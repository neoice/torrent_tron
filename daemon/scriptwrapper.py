#!/usr/bin/env python
import sys, os

# WSGI-style path setup
sys.path.append('/home/neoice/code/torrent_tron')
sys.path.append('/home/neoice/code/torrent_tron/rtorrent_interface')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
