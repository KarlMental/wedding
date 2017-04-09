from django.db import models

# Create your models here.
class Guest(models.Model):
    name = models.CharField(max_length=40)
    rsvp_answer = models.CharField(max_length=40)
    rsvp_datetime = models.TimeField(auto_created=True)
    email = models.EmailField(max_length=100)
    dietary_restrictions = models.TextField()
    shuttle = models.CharField(max_length=40)

    def __str__(self):
        return self.name
