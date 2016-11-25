# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


# This function convert a title to slug in Vietnamese
def vi_slug(data):
    vietnamese_map = {
        ord(u'o'): 'o', ord(u'ò'): 'o', ord(u'ó'): 'o', ord(u'ỏ'): 'o', ord(u'õ'): 'o', ord(u'ọ'): 'o',
        ord(u'ơ'): 'o', ord(u'ờ'): 'o', ord(u'ớ'): 'o', ord(u'ở'): 'o', ord(u'ỡ'): 'o', ord(u'ợ'): 'o',
        ord(u'ô'): 'o', ord(u'ồ'): 'o', ord(u'ố'): 'o', ord(u'ổ'): 'o', ord(u'ỗ'): 'o', ord(u'ộ'): 'o',

        ord(u'à'): 'a', ord(u'á'): 'a', ord(u'á'): 'a', ord(u'ả'): 'a', ord(u'ã'): 'a', ord(u'ạ'): 'a',
        ord(u'ă'): 'a', ord(u'ắ'): 'a', ord(u'ằ'): 'a', ord(u'ẳ'): 'a', ord(u'ẵ'): 'a', ord(u'ạ'): 'a',
        ord(u'â'): 'a', ord(u'ầ'): 'a', ord(u'ấ'): 'a', ord(u'ậ'): 'a', ord(u'ẫ'): 'a', ord(u'ẩ'): 'a',

        ord(u'đ'): 'd', ord(u'Đ'): 'd',

        ord(u'è'): 'e', ord(u'é'): 'e', ord(u'ẻ'): 'e', ord(u'ẽ'): 'e', ord(u'ẹ'): 'e',
        ord(u'ê'): 'e', ord(u'ề'): 'e', ord(u'ế'): 'e', ord(u'ể'): 'e', ord(u'ễ'): 'e', ord(u'ệ'): 'e',

        ord(u'ì'): 'i', ord(u'í'): 'i', ord(u'ỉ'): 'i', ord(u'ĩ'): 'i', ord(u'ị'): 'i',
        ord(u'ư'): 'u', ord(u'ừ'): 'u', ord(u'ứ'): 'u', ord(u'ử'): 'ữ', ord(u'ữ'): 'u', ord(u'ự'): 'u',
        ord(u'ý'): 'y', ord(u'ỳ'): 'y', ord(u'ỷ'): 'y', ord(u'ỹ'): 'y', ord(u'ỵ'): 'y',
    }
    slug = slugify(unicode(data).translate(vietnamese_map))
    return slug


class Page (models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(unique=True, blank=True, max_length=255)
    content = models.TextField(blank=True)

    def __unicode__(self):
        return self.name


class Category (models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(unique=True, blank=True, max_length=255)
    parent_category = models.CharField(max_length=255, blank=True)
    menu_index = models.IntegerField(default=0)
    url_base = models.CharField(blank=True, max_length=255)
    numberChild = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural='Categories'
        ordering = ('menu_index',)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.parent_category is None:
            try:
                parent_category = Category.objects.get(slug=self.parent_category)
                parent_category.numberChild += 1
                parent_category.save()

                if self.slug == "":
                    self.slug = vi_slug(self.name)
                else:
                    self.slug = vi_slug(self.slug)
                self.url_base = self.parent_category + "/" + self.slug
            except:
                self.url_base = self.slug
        super(Category, self).save()

    def delete(self):
        if not self.parent_category is None:
            try:
                parent_category = Category.objects.get(slug=self.parent_category)
                parent_category.numberChild-=1
                parent_category.save()
            except:
                pass
        super(Category, self).delete()


class Author(User):
    show_name = models.CharField(blank=True, max_length=255)

    class Meta:
        verbose_name_plural='Author'


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(blank=True, unique=True, max_length=255)
    content = RichTextUploadingField()
    image_thumbnail = models.ImageField(blank=True, upload_to='images/thumbnails/')
    description = models.TextField()
    keyword = models.CharField(blank=True, max_length=255)
    description = models.TextField(blank=True, max_length=255)
    is_active = models.BooleanField(default=True)
    meta_keywords = models.CharField(blank=True, max_length=255,)
    meta_description = models.CharField(blank=True, max_length=255)
    published_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)
    author = models.ManyToManyField(Author, blank=True)

    def __unicode__(self):
        return unicode(self.title)


    def save(self, *args, **kwargs):
        if self.slug == "":
            self.slug = vi_slug(self.name)
        else:
            self.slug = vi_slug(self.slug)
        super(Post, self).save(*args, **kwargs)

    def get_categories_slug (self):
        return self.categories.all().first().url_base

