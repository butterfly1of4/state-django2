from django.db import models

# Create your models here.


class Capitals(models.Model):
    state = models.CharField(max_length=150, default="state")
    capital = models.CharField(max_length=200, default="capital")
    
    def __str__(self):
        return self.state