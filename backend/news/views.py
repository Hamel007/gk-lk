# from datetime import timedelta, datetime
#
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.http import HttpResponse, Http404
#
# from django.db.models import Q, F
# from django.urls import reverse_lazy
# from django.views.generic.dates import BaseDateListView
#
# from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, View

from .models import Post


class PostList(LoginRequiredMixin, ListView):
    """Список всех новостей """
    paginate_by = 6
    template_name = "news/news-all.html"

    def get_queryset(self):
        return Post.objects.filter(published=True)


class SinglePost(LoginRequiredMixin, DetailView):
    """Полная новость"""
    model = Post
    context_object_name = 'post'

    def get_queryset(self):
        query = Post.objects.filter(slug=self.kwargs.get("slug"))
        for a in query:
            a.viewed += 1
            a.save()
        return query
