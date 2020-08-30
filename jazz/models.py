from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

class Instrument(models.Model):
		"""Model representing type of instrument."""
		instrument = models.CharField(max_length=20, help_text='Enter an instrument type')
		
		def __str__(self):
			"""String for representing the Model object"""
			return self.instrument
			
			
class Player(models.Model):
    """Model representing a player."""
    first_name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    #full_name = models.CharField(max_length=300, null = True, blank = True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    instrument = models.ForeignKey(Instrument, on_delete=models.SET_NULL, null=True, blank = True, help_text='Select instrument for this player')
    
    #--------------------------------------------------------------------------------------
    slug = models.SlugField(blank = True, unique = True) #unique=True, blank = True)
    comments = models.CharField(max_length=500, unique = False, blank = True, null = True)
    player_web = models.URLField('Web Address', blank = True)
    player_wikipedia = models.URLField('Wikipedia Page', blank = True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.full_name)
        super(Player, self).save(*args, **kwargs)
    
    @property
    def full_name(self):
        "Returns the player's full name."
        if self.nick_name is None:
            return  '%s %s' % (self.first_name, self.last_name)
        else:
            return '%s %s %s' % (self.first_name, self.nick_name, self.last_name)
    
 

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular player instance."""
        return reverse('player-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.first_name} {self.last_name}'
        
        
class Band(models.Model):
	"""Model representing a Band"""
	band_name = models.CharField(max_length=100, unique = True)
	comments = models.CharField(max_length=500, unique = False, blank = True, null = True)
	band_web = models.URLField('Web Address', blank = True) 
	slug = models.SlugField(unique=True, max_length=125 , blank = True)
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.band_name)
		super(Band, self).save(*args, **kwargs)
	
	class Meta:
		ordering = ['band_name']
		
	def get_absolute_url(self):
		"""Returns the url to access a particular band instance."""
		return reverse('band-detail', args=[str(self.id)])

	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.band_name}'
		#return f'{self.slug}'


	#def band_with_lineup_date(self):
	#	return self.lineup_set.select_related('lineup')






class Lineup(models.Model):
	"""Model representing the lineup of a band on a specified day."""
	band_name = models.ForeignKey('Band', on_delete=models.SET_NULL, null=True)
	date = models.DateField(null=True, blank=True)
	piece = models.IntegerField(null=True, blank=True)
	player = models.ManyToManyField('Player')
	comments = models.CharField('Comments', max_length=120, blank = True)
	venue = models.ForeignKey('Venue', on_delete=models.SET_NULL, null=True, blank = True, help_text='Select venue for this event')
	event = models.ForeignKey('Event', on_delete=models.SET_NULL, null=True, blank = True, help_text='Select event type')
	slug = models.SlugField(unique=True, blank = True, max_length = 125)
			
	def save(self, *args, **kwargs):
		self.slug = slugify(self.full_lineup)
		super(Lineup, self).save(*args, **kwargs)
	
	@property
	def full_lineup(self):
		"Returns the lineup's full name."
		return  '%s %s' % (self.band_name, self.date)
        
	
	class Meta:
		ordering = ['band_name', 'date']
		constraints = [models.UniqueConstraint(fields=['band_name', 'date'], name='unique_lineup')]
		
	def get_absolute_url(self):
		"""Returns the url to access a particular band instance."""
		return reverse('band_name-detail', args=[str(self.id)])

	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.band_name}, {self.date}'


class Venue(models.Model):
	"""Model representing a venue."""
	venue_name = models.CharField('Venue Name', max_length=120)
	venue_web = models.URLField('Web Address', blank = True)
	comments = models.CharField('Comments', max_length=120, blank = True)
	slug = models.SlugField(unique=True, blank = True)
	#fred = models.CharField('Venue Name', max_length=120)
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.venue_name)
		super(Venue, self).save(*args, **kwargs)

    
	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.venue_name}'

class Event(models.Model):
	"""Model representing an Event."""
	event_name = models.CharField('Event Name', max_length=120)
	date_from = models.DateField(null=True, blank=True)
	date_to = models.DateField(null=True, blank=True)
	slug = models.SlugField(unique=False, blank = True)
	event_web = models.URLField('Web Address', blank = True)
	comments = models.CharField('Comments', max_length=120, blank = True)

	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.event_name}'

	def save(self, *args, **kwargs):
		self.slug = slugify(self.event_name)
		super(Event, self).save(*args, **kwargs)
		
		
#class Role(models.Model):
#	lineup = models.ForeignKey(Lineup, on_delete=models.DO_NOTHING)
#	player = models.ForeignKey(Player, on_delete=models.DO_NOTHING)
