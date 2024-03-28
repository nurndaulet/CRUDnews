from djongo import models
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='img/')

    def __str__(self):
        return self.title