from django.db import models

# Create your models here.

class Section(models.Model):
    section_name = models.CharField(max_length= 100)

    def __str__(self) -> str:
        return self.section_name



class New_Menu(models.Model):
    section_name = models.ForeignKey(Section,on_delete=models.DO_NOTHING)
    menu_name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='media')
    food_name = models.CharField(max_length=100)
    food_info = models.TextField()
    price = models.IntegerField()



    def __str__(self) -> str:
        return f"{self.food_name} -- {self.price} -- {self.section_name}"







