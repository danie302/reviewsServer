from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=25)
    image = models.FileField(upload_to='city/', max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    review = models.TextField()
    city = models.CharField(max_length=25)
    traveller = models.CharField(max_length=50)
    image = models.FileField(upload_to='review/', max_length=100, blank=True, null=True)

    def __str__(self):
        return self.traveller