from django.db import models

# Create your models here.
class Food(models.Model):
    recipe_name = models.CharField(max_length=500)
    recipe_description = models.TextField( null=True)
    recipe_image = models.ImageField(upload_to="food_images" ,null=True , blank=True , default="")

