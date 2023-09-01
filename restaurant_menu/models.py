from typing import Any
from django.db import models
from django.contrib.auth.models import User

MEAL_TYPE = (
    ("starter", "Starter"),
    ("salad", "Salad"),
    ("main_dishes", "Main Dishes"),
    ("desserts", "Desserts"),
    ("drinks", "Drinks"),
)

STATUS = (
    (0, "Unavailable"),
    (1, "Available"),
)


class Items(models.Model):
    meal = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    meal_type = models.CharField(choices=MEAL_TYPE, max_length=200)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.IntegerField(default=1, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.meal
