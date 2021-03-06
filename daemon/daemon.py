#!/usr/bin/env python
import scriptwrapper

# models
from rtorrent_interface.models import Torrent

# django
from django.shortcuts import get_object_or_404

# rtorrent setup
import xmlrpc2scgi as xs
rtorrent_host='scgi://127.0.0.1:5000'
rt = xs.RTorrentXMLRPCClient(rtorrent_host)

### start
# TODO: switch to multi-call for performance
for torrent_hash in rt.download_list(""):

    torrent, bool = Torrent.objects.get_or_create(torrent_hash=torrent_hash)
    torrent.torrent_name    = rt.d.get_name(torrent_hash)
    torrent.rate_up         = 0
    torrent.rate_down       = 0
    torrent.speed_up        = rt.d.get_up_rate(torrent_hash)
    torrent.speed_down      = rt.d.get_down_rate(torrent_hash)

    torrent.save()
