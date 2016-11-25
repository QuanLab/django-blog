# -*- coding: utf-8 -*-
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Category, Post
from myblog import settings


def get_context_custom():
    context = {
        'menu': Category.objects.all().filter(parent_category=""),
        'sub_menu': Category.objects.all().filter(numberChild=0),
        'featured_post': Post.objects.all().order_by('?')[:5],
        'title': settings.PAGE_TITLE
    }
    return context


class Index(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        post_list = Post.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(post_list, settings.NUMBER_POST_PER_PAGINATOR)

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context = get_context_custom()
        context.update({
            'posts': posts
        })
        return render(request, self.template_name, context)


class CategoryView(View):
    template_name = 'index.html'

    def get(self, request, category_slug):
        context = get_context_custom()
        try:
            post_list = get_object_or_404(Category, url_base=category_slug).post_set.all()
            page = request.GET.get('page', 1)
            paginator = Paginator(post_list, settings.NUMBER_POST_PER_PAGINATOR)

            try:
                posts = paginator.page(page)
            except PageNotAnInteger:
                posts = paginator.page(1)
            except EmptyPage:
                posts = paginator.page(paginator.num_pages)

            context = get_context_custom()
            context.update({
                'posts': posts
            })
            context.update({
                'posts': posts
            })
            return render(request, self.template_name, context)
        except:
            return render(request, self.template_name, context)


class PostDetails(View):
    template_name = 'post/post_detail.html'

    def get(self, request, category_slug=None, post_slug=None):
        post = get_object_or_404(Post, slug=post_slug)
        context = get_context_custom()
        context.update({
            'post': post
        })
        return render(request, self.template_name, context)
