from django.db import models

class Squirrel(models.Model):
    
    SHIFT_CHOICES = [
            ('AM', 'AM'),
            ('PM', "PM"),
    ]
    
    AGE_CHOICES = [
            ('adult', 'Adult'),
            ('junvenile', "Juvenile"),
    ]
                
    longitude = models.FloatField("Longitude")
    
    latitude = models.FloatField("Latitude")

    squirrel_id = models.CharField("Unique Squirrel ID", unique = True)
    
    shift = models.CharField("Shift", max_length = 16, choices = SHIFT_CHOICES)
    
    date = models.DateField('Date')
    
    age = models.CharField("Age", max_length = 64, choices = AGE_CHOICES)

