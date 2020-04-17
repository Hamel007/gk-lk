# coding=utf-8
from django.urls import path
from backend.profile import views

urlpatterns = [
    path("", views.MembersCollective.as_view(), name="members_list"),
    path("partner/", views.PartnerCollective.as_view(), name="partner_list"),
    path("queue/", views.Turn.as_view(), name="turn_list"),
    path("deal/", views.Deal.as_view(), name="deal_list"),
    path("calculated/", views.Calculated.as_view(), name="calculated_list"),
    path("debtor/", views.Debtor.as_view(), name="debtor_list"),
]
