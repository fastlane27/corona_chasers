from django.db import models
from django.contrib.auth.models import User

class Global(models.Model):
    name = models.CharField()
    infected = models.IntegerField()
    deaths = models.IntegerField()
    recovered = models.IntegerField()
    last_updated = models.DateTimeField()

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField()
    infected = models.IntegerField()
    deaths = models.IntegerField()
    recovered = models.IntegerField()

    def __str__(self):
        return self.name

class Comment(models.Model):
    posted_at = models.DateTimeField()
    content = models.TextField(max_length=250)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment {self.id} by {self.created_by.username}'

class Province(models.Model):
    name = models.CharField()
    infected = models.IntegerField()
    deaths = models.IntegerField()
    recovered = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name