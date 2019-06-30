from django.db import models
from django.utils import timezone


class BoastRoastModel(models.Model):
    # boast = models.CharField(max_length=280, blank=True)
    # roast = models.CharField(max_length=280, blank=True)
    # could do a pick between oast and roast
    # one post for baost rastL https://stackoverflow.com/questions/4320679/django-display-choice-value
    B = "B"
    R = "R"
    BOAST_OR_ROAST = ((B, "Boast"), (R, "Roast"))
    choice = models.CharField(max_length=280, choices=BOAST_OR_ROAST, default=B)
    post = models.CharField(max_length=280, default="Write a boast or roast")
    # date = models.DateTimeField(default=timezone.now)
    # dont need many to many b/c not indepth
    # do 2 of each or just vote count field
    # capture ip adress of whoever votes to check against stuff
    upvotes = models.PositiveIntegerField(default=0, blank=True)
    downvotes = models.PositiveIntegerField(default=0, blank=True)

    def __str__(self):
        return f"{self.choice}: {self.post}"
