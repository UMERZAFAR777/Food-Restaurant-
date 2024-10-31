from django.db import models

# Create your models here.

class Custom_Birthday(models.Model):
    img = models.ImageField(upload_to='media')
    custom_name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self) -> str:
        return self.custom_name 






