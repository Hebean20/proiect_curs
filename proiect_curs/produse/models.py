from django.db import models

class Products(models.Model):
    product = models.CharField(max_length=100)
    stoc_disponibil = models.IntegerField(default=0)

    def __str__(self):
        return self.product + '-->' + str(self.stoc_disponibil)