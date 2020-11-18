from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name='polls'

urlpatterns = [
    path('', views.HomeView.as_view()),
]
