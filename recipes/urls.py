from django.urls import path
from . import views
from django.views.generic import TemplateView

appname = "recipes"
urlpatterns=[
    path("",views.MainView.as_view(),name="all")
]