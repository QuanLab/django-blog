from django.contrib import admin
from . models import *


admin.site.register(Category)

admin.site.register(Post)

admin.site.register(Page)

admin.site.register(Author)