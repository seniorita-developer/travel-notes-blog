from django.db import models
from django.contrib.auth.models import User


class Destination(models.Model):
    text = models.CharField(max_length=70)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Entry(models.Model):
    destination = models.ForeignKey(
        'Destination',
        on_delete=models.CASCADE,
    )
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        if len(self.text) > 50:
            return self.text[:50] + '...'
        else:
            return self.text


