# coding=utf-8
from django.urls import path
from backend.feedback import views

app_name = "feedback"
urlpatterns = [
    path("create/", views.FeedbackCreate.as_view(), name="create"),
    path("", views.FeedbackList.as_view(), name="feedback"),
]
