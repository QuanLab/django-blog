# -*- coding: utf-8 -*-
from django.views import View
from django.shortcuts import render, get_object_or_404
from . models import Category, Post
from myblog import settings


def get_context_custom():

    context = {
        'menu':Category.objects.all().filter(parent_category=""),
        'sub_menu': Category.objects.all().filter(numberChild=0),
        'featured_post':Post.objects.all().order_by('?')[:5],
        'title': settings.PAGE_TITLE
    }
    return context


class MyFormView(View):

    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        all_post = Post.objects.all()
        context = get_context_custom()
        context.update({
            'all_post':all_post
        })
        return render(request, self.template_name, context)


class CategoryView (View):

    template_name = 'index.html'

    def get(self, request, category_slug):
        context = get_context_custom()
        try:
            all_post = get_object_or_404(Category, slug=category_slug).post_set.all()
            context.update({
                'all_post': all_post
            })
            return render(request, self.template_name, context)
        except:
            return render(request, self.template_name, context)


class PostDetails (View):

    template_name = 'post/post_detail.html'

    def get(self, request, category_slug=None, post_slug=None):
        post = get_object_or_404(Post, slug=post_slug)
        context = get_context_custom()
        context.update({
            'post': post
        })
        return render(request, self.template_name, context)
