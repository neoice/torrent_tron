from django.db import models

class Torrent(models.Model):
    torrent_hash    = models.CharField(max_length=255, primary_key=True)
    torrent_name    = models.CharField(max_length=1023, default='')

    """ all values are in $x kB """
    # data value caps
    rate_up         = models.IntegerField(null=True, default=0)
    rate_down       = models.IntegerField(null=True, default=0)
    # current speed of the upload/download
    speed_up        = models.IntegerField(null=True, default=0)
    speed_down      = models.IntegerField(null=True, default=0)

    active          = models.BooleanField(default=False)

class Tracker(models.Model):
    tracker_name    = models.CharField(max_length=255)
    tracker_url     = models.CharField(max_length=255)

    remembered = models.BooleanField(default=False)
