from django.shortcuts import render
from django.views import generic
from django.db.models import Count

from jazz.models import Player, Lineup, Band, Venue, Event

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_players = Player.objects.all().count()
    num_lineups = Lineup.objects.all().count()
    num_bands = Band.objects.all().count()
    num_venus = Venue.objects.all().count()
    num_events = Event.objects.all().count()
    top_players = Lineup.objects.values('player', 'player__first_name', 'player__nick_name', 'player__last_name', 'player__slug').annotate(c=Count('player')).order_by('-c') [:10]
        
    context = {
        'num_players': num_players,
        'num_lineups': num_lineups,
        'num_bands': num_bands,
        'num_venus': num_venus,
        'num_events': num_events,
        'top_players': top_players,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BandListView(generic.ListView):
	model = Band


class BandDetailView(generic.DetailView):
    model = Band


class PlayerListView(generic.ListView):
	model = Player

class PlayerDetailView(generic.DetailView):
    model = Player


class VenueListView(generic.ListView):
	model = Venue

class VenueDetailView(generic.DetailView):
    model = Venue


class EventListView(generic.ListView):
	model = Event

class EventDetailView(generic.DetailView):
    model = Event

class LineupListView(generic.ListView):
	model = Lineup

class LineupDetailView(generic.DetailView):
    model = Lineup



#Person.objects.values('optional_first_name').annotate(c=Count('optional_first_name')).order_by('-c')
