from django.contrib import admin
from . models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')

admin.site.register(Category)

admin.site.register(Post, PostAdmin)

admin.site.register(Author)

admin.site.register(Setting)