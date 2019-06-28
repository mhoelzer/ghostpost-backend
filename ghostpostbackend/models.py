from django.db import models
from django.utils import timezone


class BoastRoastModel(models.Model):
    # could do a pick between oast and roast 
    # one post for baost rast 
    boast = models.CharField(max_length=280, blank=True)
    roast = models.CharField(max_length=280, blank=True)
    # date = models.DateTimeField(default=timezone.now)
    # do 2 of each or just vote count field
    # capture ip adress of whoever votes to check against stuff
    upvotes = models.PositiveIntegerField(default=0, blank=True)
    downvotes = models.PositiveIntegerField(default=0, blank=True)
    # dont need many to many b/c not indepth
    # upvotes = models.ManyToManyField("self", symmetrical=False, blank=True, related_name="up")
    # downvotes = models.ManyToManyField("self", symmetrical=False, blank=True, related_name="down")

    # def __str__(self):
    #     return self.date
