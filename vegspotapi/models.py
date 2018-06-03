from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    """
    A person object represents a user that has a profile saved.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)


class Venue(models.Model):
    """
    A venue object represents a company that sells any kind of vegan food.
    """
    name = models.CharField(max_length=50)
    responsible = models.ForeignKey(Person, on_delete=models.CASCADE)
    description = models.TextField()


class Review(models.Model):
    """
    A review object represents an evaluation from a user to a company
    """
    author = models.ForeignKey(Person, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    star = models.IntegerField()
    content = models.TextField()

