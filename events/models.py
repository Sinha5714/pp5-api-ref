from django.db import models
from django.contrib.auth.models import User

EVENT_CATEGORIES = (
    ("Discrimination", "Descrimination"),
    ("LQBTQ", "LGBTQ"),
    ("Equal-Rights", "Equal Rights"),
    ("Marraige", "Marraige"),
    ("Work", "Work"),
    ("Education", "Education"),
)

EVENT_SUB_CATEGORIES = (
    ("Seminars", "Seminars"),
    ("Webinars", "Webinars"),
    ("Retreats", "Retreats"),
)


class Event(models.Model):
    """
    Event model for events posted by users, related to User
    """
    image_filter_choices = [
        ('_1977', '1977'), ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'), ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'), ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'), ('normal', 'Normal'),
        ('nashville', 'Nashville'), ('rise', 'Rise'),
        ('toaster', 'Toaster'), ('valencia', 'Valencia'),
        ('walden', 'Walden'), ('xpro2', 'X-pro II')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    country = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../equal-rights_o1owqr', blank=True
    )
    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='Normal'
    )
    event_date = models.DateField(blank=False)
    category = models.CharField(
        max_length=50, choices=EVENT_CATEGORIES, default='Equal-Rights'
    )
    sub_category = models.CharField(
        max_length=50, choices=EVENT_SUB_CATEGORIES, default='Seminars'
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.id} {self.title}'
