from django.urls import path
from . import views
from mi_app.views import index

urlpatterns = [
    path('', views.index, name='index'),
]