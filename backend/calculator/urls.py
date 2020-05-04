from django.urls import path
from backend.calculator import views

urlpatterns = [
    path("", views.CalculatorView.as_view(), name="calculator"),
    path('ajax/get_response/', views.answer_me, name='get_response')
]