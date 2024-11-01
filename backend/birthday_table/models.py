from django.db import models

# Create your models here.

class Custom_Table(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField()
    date = models.DateField()
    time = models.TimeField() 
    people = models.IntegerField()
    message = models.TextField()





    def __str__(self) -> str:
        return f"{self.name} -- {self.date} -- {self.time}" 








