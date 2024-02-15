from django.db import models

# Products | Model.


class Product(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    trending = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    price = models.FloatField(default=0.00)

    def __str__(self):
        return str(self.name)
