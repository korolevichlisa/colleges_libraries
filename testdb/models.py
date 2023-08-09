# from statistics import mode
# from turtle import title

from distutils.command.upload import upload
# from turtle import title
from django.template.defaultfilters import slugify
import os

from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class College(models.Model):
    name_college = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name_college

class New(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField()
    id_college = models.ForeignKey(College, on_delete=models.CASCADE)
    created_date = models.DateField(
        default=timezone.now)

    update_date = models.DateField(blank=True, null=True)

    def upd(self):
        self.update_date = timezone.now()
        self.save()

    published_date = models.DateField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # def __str__(self):
    #     return super().__str__()
    

class Coworkers(models.Model):
    full_name = models.CharField(max_length=250)
    text = models.TextField()
    photo = models.ImageField(upload_to ='image/')
    id_college = models.ForeignKey(College, on_delete=models.CASCADE)
    created_date = models.DateField(
        default=timezone.now)

    update_date = models.DateField(blank=True, null=True)

    def upd(self):
        self.update_date = timezone.now()
        self.save()

    published_date = models.DateField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


class Library_funds(models.Model):
#     title = models.CharField(max_length=200)
#     position = models.CharField(max_length=150)
    text = models.TextField()
    # photo = models.ImageField(upload_to ='uploads/')
    id_college = models.ForeignKey(College, on_delete=models.CASCADE)
    created_date = models.DateField(
        default=timezone.now)

    update_date = models.DateField(blank=True, null=True)

    def upd(self):
        self.update_date = timezone.now()
        self.save()

    published_date = models.DateField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()



class Library_room(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    # photo = models.ImageField(upload_to ='uploads/')
    # id_photo = models.ForeignKey(Photos, on_delete=models.CASCADE)
    image = models.FileField(blank=True)
    id_college = models.ForeignKey(College, on_delete=models.CASCADE)
    created_date = models.DateField(
        default=timezone.now)

    update_date = models.DateField(blank=True, null=True)

    def upd(self):
        self.update_date = timezone.now()
        self.save()

    published_date = models.DateField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class Photos(models.Model):
    photo = models.ImageField(upload_to ='uploads/')
    # text = models.TextField()
    post = models.ForeignKey(Library_room, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.post.title

class Library_servic(models.Model):
    name_services = models.CharField(max_length=200)
    # price_count = models.IntegerField()
    id_college = models.ForeignKey(College, on_delete=models.CASCADE)
    created_date = models.DateField(
        default=timezone.now)

    update_date = models.DateField(blank=True, null=True)

    def upd(self):
        self.update_date = timezone.now()
        self.save()

    published_date = models.DateField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class Exhibition(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField()
    photo = models.ImageField(upload_to ='uploads/')
    doc = models.FileField(upload_to ='uploads/')
    id_college = models.ForeignKey(College, on_delete=models.CASCADE)
    created_date = models.DateField(
        default=timezone.now)

    update_date = models.DateField(blank=True, null=True)

    def upd(self):
        self.update_date = timezone.now()
        self.save()

    published_date = models.DateField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()