import os
import random

from django.db import models
from User.models import User



class Category(models.Model):
    title = models.CharField(max_length=100)

class Tag(models.Model):
    tag = models.CharField(max_length=100)


def get_item_image_path(instance, filename):
    filename = str(random.randint(10000, 100000)) + filename
    path = 'item_images/%s' % (filename)

    return path

class Item(models.Model):
    categories = models.ManyToManyField(Category, related_name='items')
    tags = models.ManyToManyField(Tag, related_name='items')
    title = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=get_item_image_path)


# class CategoryItem(models.Model):
#     category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
#     item = models.ForeignKey(Item, related_name='categories',on_delete=models.CASCADE)


class UserItem(models.Model):
    user = models.ForeignKey(User,related_name='items',on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)


class History(models.Model):
    user = models.ForeignKey(User, related_name='histories', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    is_refunded = models.BooleanField(default=False)


class HistoryItem(models.Model):
    history = models.ForeignKey(History, related_name='items', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)