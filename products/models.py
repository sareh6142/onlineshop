from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    #cover = models.ImageField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', ars=[self.pk])



class Comment(models.Model):
    PRODUCT_STARS = [
            ('1', 'very Bad'),
            ('2', 'Bad'),
            ('3', 'Normal'),
            ('4', 'Good'),
            ('5', 'very Good'),
        ]
    body = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    stars = models.CharField(max_length=10, choices=PRODUCT_STARS)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    #product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')


