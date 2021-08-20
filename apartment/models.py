from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Apartment(models.Model):
    name = models.CharField(max_length=514)
    region = models.CharField(max_length=514)
    cost =  models.IntegerField(
        verbose_name='',
        blank=True,
        null=True,
        default=0,
        validators=[MinValueValidator(0),
                    MaxValueValidator(100000)]
    )
    room =  models.IntegerField(
        verbose_name='',
        blank=True,
        null=True,
        default=0,
        validators=[MinValueValidator(0),
                    MaxValueValidator(1000)]
    )
    image = models.ImageField(upload_to='images',blank=True, null=True)
    information = models.TextField()
    features_flag = models.IntegerField(
        verbose_name='',
        default=0,
        validators=[MinValueValidator(0),
                    MaxValueValidator(1)]
    )
    main_flag = models.IntegerField(
        verbose_name='',
        default=0,
        validators=[MinValueValidator(0),
                    MaxValueValidator(1)]
    )

    def __str__(self):
        return self.name
