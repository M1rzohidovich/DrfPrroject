from os.path import splitext

from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


def slugify_upload(instance, filename):
    folder = instance._meta.model.__name__
    name, ext = splitext(filename)
    try:

        name_t = slugify(name)
        if name_t is None:
            name_t = name
        path = folder + "/" + name_t + ext
    except:
        path = folder + "/default" + ext

    return path


class Region (models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regions"

    def __str__(self) :
        return self.name  


class District(models.Model):
    name = models.CharField(max_length=40)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Distirict"
        verbose_name_plural = "Distiricts"

    def __str__(self):
        return self.name


class Announcement(models.Model):
    announce_type = (
        ('Sale', 'Sale'),
        ('Rent', 'Rent')
    )
    announce_view = (
        ('Flat', 'Flat'),
        ('House', 'House'),
        ('Office', 'Office'),
    )
    announcement_condition = (
        ('New', 'New'),
        ('Used', 'Used')
    )
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    address = models.CharField(max_length=150)
    remaining_information = models.TextField()
    description = models.TextField()
    type = models.CharField(choices=announce_type, max_length=4)
    view = models.CharField(choices=announce_view, max_length=6)
    condition = models.CharField(choices=announcement_condition, max_length=4)
    img1 = models.ImageField(upload_to = slugify_upload)
    img2 = models.ImageField(upload_to = slugify_upload, blank=True)
    img3 = models.ImageField(upload_to = slugify_upload, blank=True)
    img4 = models.ImageField(upload_to = slugify_upload, blank=True)
    img5 = models.ImageField(upload_to = slugify_upload, blank=True)
    price = models.FloatField()
    upload_date = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Announcement"
        verbose_name_plural = "Announcements"
    
    def __str__(self):
        return self.type


class Blog(models.Model):
    title = models.CharField(max_length=60)
    img = models.ImageField(upload_to=slugify_upload)
    desctiption = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField()

    def __str__(self):
        return self.title

