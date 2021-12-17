from django.db import models

# Create your models here.
class Drink(models.Model):
    purchaser = models.CharField(max_length=50)
    bar = models.CharField(max_length=50)
    date = models.CharField(max_length=20)

    def __str__(self):
        return self.purchaser + " | " + self.bar + " | " + self.date