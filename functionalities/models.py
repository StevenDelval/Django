from django.db import models

# Create your models here.
class Functionalities(models.Model):
    name=models.CharField(
        max_length=100,
        null=False
    )

    description = models.TextField(
        max_length=500
    )

    def __str__(self):
        return "{0} -- {1}...".format(self.name,self.description[0:30])
    
    