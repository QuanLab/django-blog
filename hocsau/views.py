# -*- coding: utf-8 -*-
from django.views import View
from django.shortcuts import render, get_object_or_404
from . models import Category, Post
from myblog import settings


def get_all_categories():
    return Category.objects.all()


class MyFormView(View):

    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        all_post = Post.objects.all()
        return render(request, self.template_name,
                      {'all_post': all_post, 'menu_item': get_all_categories(), 'title': settings.PAGE_TITLE})


class CategoryView (View):

    template_name = 'index.html'

    def get(self, request, category_slug):
        all_post = get_object_or_404(Category, slug=category_slug).post_set.all();
        return render(request, self.template_name,
                      {'all_post': all_post, 'menu_item': get_all_categories(), 'title':settings.PAGE_TITLE})


class PostDetails (View):

    template_name = 'post/post_detail.html'

    def get(self, request, category_slug=None, post_slug=None):
        post = get_object_or_404(Post, slug=post_slug)
        return render(request, self.template_name,
                      {'post': post, 'menu_item': get_all_categories(), 'title': settings.PAGE_TITLE})
