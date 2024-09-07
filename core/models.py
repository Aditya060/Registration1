from django.db import models

class User(models.Model):
    VENUE_CHOICES = [
        ('venue1', 'Venue 1'),
        ('venue2', 'Venue 2'),
        ('venue3', 'Venue 3'),
        ('venue4', 'Venue 4'),
        ('venue5', 'Venue 5'),
    ]
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default = None )
    venue = models.CharField(max_length=10, choices=VENUE_CHOICES, default = None)

    def __str__(self):
        return self.name
