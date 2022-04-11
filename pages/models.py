from django.db import models

# Create your models here.

class TopBar(models.Model):
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return str(self.phone)