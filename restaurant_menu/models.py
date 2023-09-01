from django.db import models
from django.contrib.auth.models import User

MEAL_TYPE = (
    ("starter", "Starter"),
    ("salad", "Salad"),
    ("main_dishes", "Main Dishes"),
    ("desserts", "Desserts"),
    ("drinks", "Drinks"),
)


class Items(models.Model):
    meal = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(decimal_places=2)
    meal_type = models.CharField(choices=MEAL_TYPE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


