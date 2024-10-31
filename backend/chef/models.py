from django.db import models

# Create your models here.

class Chef(models.Model):
    img = models.ImageField(upload_to='media')
    chef_name = models.CharField(max_length=100)
    chef_title = models.CharField(max_length=100)
    chef_des = models.TextField()


    def __str__(self) -> str:
        return self.chef_name




