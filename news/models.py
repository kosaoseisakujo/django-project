from django.db import models
from django.utils import timezone

# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=514)
    image = models.ImageField(upload_to='images',blank=True, null=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
