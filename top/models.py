from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    main_flag = models.IntegerField(
        verbose_name='',
        default=0,
        validators=[MinValueValidator(0),
                    MaxValueValidator(1)]
    )

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images',blank=True, null=True)
    text = models.TextField()

    def __str__(self):
        return self.name
