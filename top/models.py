from django.db import models

# Create your models here.
class MainMenu(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images',blank=True, null=True)
    text = models.TextField()

    def __str__(self):
        return self.name
