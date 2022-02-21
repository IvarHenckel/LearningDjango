from django.db import models
from django.urls import reverse

# Create your models here.

# IH: we store data of products in a database
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField() #models.TextField(default='this is c')
    # IH: Note: If we want to add a new field to an existing table in the database
    # we have to use null=True or default=.... which will then be applied to all old entries.
    # migrating -> informing the db off changes in our model (database)

    def get_absolute_url(self):
        return reverse("products:product", kwargs={"id": self.id}) #f"/products/{self.id}/"
