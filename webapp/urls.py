from django.urls import path
from webapp import views
urlpatterns = [
    path('', views.home, name="show_home"),
]