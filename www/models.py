from django.db import models

# Create your models here.
class Guest(models.Model):
    RSVP_ANSWER_CHOICES = (('Kommer', 'Kommer'), ('Kommer Inte', 'Kommer Inte'))
    SHUTTLE_CHOICES = (
    ('NEJ', 'Nej'), ('DIT', 'Bara dit'), ('DIT2300', 'Dit och hem 23:00'), ('DIT0030', 'Dit och hem 00:30'),
    ('DIT0200', 'Dit och hem 02:00'))

    name = models.CharField(max_length=40, verbose_name='Namn (För- och Efternamn)')
    rsvp_answer = models.CharField(max_length=40, verbose_name='OSA', choices=RSVP_ANSWER_CHOICES)
    rsvp_datetime = models.TimeField(auto_now_add=True, blank=True)
    email = models.EmailField(max_length=100)
    dietary_restrictions = models.TextField(verbose_name='Specialkost', blank=True)
    shuttle = models.CharField(max_length=40, choices=SHUTTLE_CHOICES, verbose_name='Vill du åka buss? (om du vill åka buss på hemvägen ge gärna en gissning på vilken buss du vill ta)')

    def __str__(self):
        return self.name
