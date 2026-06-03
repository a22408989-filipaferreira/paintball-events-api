from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="participants"
    )

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    participants = models.ManyToManyField(
        Participant,
        related_name="teams",
        blank=True
    )

    def __str__(self):
        return self.name