from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from uuid import uuid4


class Natal(models.Model):
    """ Data for the natal chart of the person
        http://humandes.ru/astroserviceprog.html - natal zodiak 
    """
    user = models.ForeignKey(User)
    uuid = models.CharField(max_length=255, unique=True, null=False, 
                            blank=False, editable=False, default=uuid4)
    person = models.CharField('Person name', 
        max_length=50, blank=False)
    birth_date_time = models.CharField('Birth date', 
        max_length=50,)
    birth_place = models.CharField('Birth place', 
        max_length=255, default='Moscow')
                                            
    birth_latitude = models.FloatField('Birth latitude', 
        default=55.75, blank=True, null=True)
    birth_longitude = models.FloatField('Birth longitude', 
        default=37.62, blank=True, null=True)    
    sun = models.CharField('Sun', 
        max_length=20, blank=True, null=True)
    moon = models.CharField('Moon', 
        max_length=20, blank=True, null=True)
    mercury = models.CharField('Mercury', 
        max_length=20, blank=True, null=True)
    venus = models.CharField('Venus', 
        max_length=20, blank=True, null=True)
    mars = models.CharField('Mars', 
        max_length=20, blank=True, null=True)
    jupiter = models.CharField('Jupiter', 
        max_length=20, blank=True, null=True)
    saturn = models.CharField('Saturn', 
        max_length=20, blank=True, null=True)
    uran = models.CharField('Uran', 
        max_length=20, blank=True, null=True)
    neptun = models.CharField('Neptun', 
        max_length=20, blank=True, null=True)
    pluto = models.CharField('Pluto', 
        max_length=20, blank=True, null=True)
    created_date = models.DateTimeField('Date of creation', 
                                            default=timezone.now())
    updated_date = models.DateTimeField('Date of update', 
                                            default=timezone.now())

    def __str__(self):
        return self.person

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"
        ordering = ["-created_date"]


