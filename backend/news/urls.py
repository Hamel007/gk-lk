# coding=utf-8
from django.urls import path
from backend.news import views

urlpatterns = [
    path("<slug:slug>/", views.SinglePost.as_view(), name="single_post"),
    path("", views.PostList.as_view(), name="news"),
]
