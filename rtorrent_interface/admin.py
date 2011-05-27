from django.contrib import admin, messages
from models import Torrent, Tracker

class TorrentAdmin(admin.ModelAdmin):
    list_display = ( 'torrent_name',
                     'RateUp_Converter', 'RateDown_Converter',
                     'SpeedUp_Converter', 'SpeedDown_Converter' )

    def ByteConverter(self, obj, value):
        # TODO: make configurable off a DB setting
        # we only do Mbps for now
        Mbps = float(value) * 0.008192

        return str(Mbps) + " Mbps"

    # TODO: simplify / condense?
    def RateUp_Converter(self, obj):
        return self.ByteConverter(self, obj.rate_up)
    def RateDown_Converter(self, obj):
        return self.ByteConverter(self, obj.speed_up)
    def SpeedUp_Converter(self, obj):
        return self.ByteConverter(self, obj.speed_up)
    def SpeedDown_Converter(self, obj):
        return self.ByteConverter(self, obj.speed_down)

    RateUp_Converter.short_description = "Upload Cap"
    RateDown_Converter.short_description = "Download Cap"
    SpeedUp_Converter.short_description = "Seeding Speed"
    SpeedDown_Converter.short_description = "Leeching Speed"

admin.site.register(Torrent, TorrentAdmin)
admin.site.register(Tracker)
