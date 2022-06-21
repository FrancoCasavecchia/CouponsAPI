from django.db import models

# Create your models here.

class Coupons(models.Model):
    code = models.CharField(max_length=60,unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField()
    active = models.BooleanField()


    def __str__(self):
        return self.code
