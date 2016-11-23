# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.contrib.auth.models import User
# from ckeditor.fields import RichTextField


class Page (models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(unique=True,max_length=255)
    content = models.TextField(blank=True)

    def __unicode__(self):
        return self.name


class Category (models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(unique=True, max_length=255)
    parent_category = models.CharField(max_length=255, blank=True)
    menu_index = models.IntegerField(default=0)
    hasChild= models.BooleanField(default=False)

    class Meta:
        verbose_name_plural='Categories'
        ordering = ('menu_index',)

    def __unicode__(self):
        return self.name


class Author(User):
    show_name = models.CharField(blank=True, max_length=255)
    class Meta:
        verbose_name_plural='Author'


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(unique=True, max_length=255)
    content = RichTextUploadingField()
    image_thumbnail = models.ImageField(blank=True, upload_to='images/thumbnails/')
    description = models.TextField()
    keyword = models.CharField(blank=True, max_length=255)
    description = models.TextField(blank=True, max_length=255)
    is_active = models.BooleanField(default=True)
    meta_keywords = models.CharField(blank=True, max_length=255,)
    meta_description = models.CharField(blank=True, max_length=255)
    published_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category)
    author = models.ManyToManyField(Author, blank=True)

    def __unicode__(self):
        return unicode(self.title)

    def get_categories_slug (self):
        return self.categories.all().first().slug