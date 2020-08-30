from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('bands/', views.BandListView.as_view(), name='bands'),
	path('bands/<slug:slug>', views.BandDetailView.as_view(), name='band-detail'),
	path('players/', views.PlayerListView.as_view(), name='players'),
    path('players/<slug:slug>', views.PlayerDetailView.as_view(), name='player-detail'),
    path('venues/', views.VenueListView.as_view(), name='venues'),
    path('venues/<slug:slug>', views.VenueDetailView.as_view(), name='venue-detail'),
    path('events/', views.EventListView.as_view(), name='events'),
    path('events/<slug:slug>', views.EventDetailView.as_view(), name='event-detail'),
    path('lineups/', views.LineupListView.as_view(), name='lineups'),
    path('lineups/<slug:slug>', views.LineupDetailView.as_view(), name='lineup-detail'),
]
