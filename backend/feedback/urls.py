# coding=utf-8
from django.urls import path
from backend.feedback import views

app_name = "feedback"
urlpatterns = [
    path("create/", views.FeedbackCreate.as_view(), name="create"),
    path("all_support/", views.FeedbackAdminList.as_view(), name="feedback_admin"),
    path("single_support/<int:pk>/", views.FeedbackDetail.as_view(), name="feedback_single"),
    path("", views.FeedbackList.as_view(), name="feedback"),
]
