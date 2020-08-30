from django.contrib import admin

from jazz.models import Instrument
from jazz.models import Player
from jazz.models import Band
from jazz.models import Lineup
from jazz.models import Venue
from jazz.models import Event
#from jazz.models import Role

class membershipInline(admin.TabularInline):
    model = Lineup.player.through
	
class PlayerAdmin(admin.ModelAdmin):
    inlines = [
			membershipInline,
   ]

class LineupAdmin(admin.ModelAdmin):
    inlines = [
        membershipInline,
    ]
    exclude = ('player',)
    list_display = ('band_name', 'slug', )


class LineupAdminInline(admin.TabularInline):
	model = Lineup
	exclude = [ 'player', ]
	
class VenueAdmin(admin.ModelAdmin):
	inlines = ( LineupAdminInline, )
	list_display = ('venue_name', 'slug',)
	
class EventAdmin(admin.ModelAdmin):
	inines = ( LineupAdminInline, )

class BandAdmin(admin.ModelAdmin):
	model = Band
	list_display = ('band_name', )



admin.site.register(Instrument)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Band, BandAdmin)
admin.site.register(Lineup, LineupAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Event)
#admin.site.register(Role)
