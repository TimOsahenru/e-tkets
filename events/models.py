from django.db import models


class Event(models.Model):

    COUNTRY_CHOICES = (
        ('nigeria', 'Nigeria'),
        ('ghana', 'Ghana'),
        ('usa', 'United States of America')
    )

    EVENT_CHOICES = (
        ('chidren', 'Children & Youth'),
        ('fashion', 'Fashion & Design'),
        ('media', 'Media & Gym'),
        ('sport', 'Sport & Fitness'),
        ('government', 'Government'),
        ('community', 'Community'),
        ('charity', 'Charity & Aid'),
        ('school', 'School & Education'),
        ('career', 'Career'),
        ('spirituality', 'Spirituality & Religion'),
        ('investments', 'Investments'),
        ('business', 'Business'),
        ('technology', 'Technology & Science'),
        ('startups', 'Startups & Small Business'),
        ('foods', 'Foods & Drink'),
        ('art', 'Art & Culture'),
        ('music', 'Music & Performance')
    )
    name = models.CharField(max_length=150)
    # event_creator(PK) = 
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=150)
    location_tips = models.CharField(max_length=150)
    call_for_direction = models.CharField(max_length=30)
    country = models.CharField(max_length=15, choices=COUNTRY_CHOICES, default='nigeria')

    event_type = models.CharField(max_length=50, choices=EVENT_CHOICES, default='business')
    # social_media_handles = 
    # custom_event_url = 
    # image = 
    is_free = models.BooleanField(default=True)
    # tickets(PK) = 

# if is_free == False
    # redirect to ticket page