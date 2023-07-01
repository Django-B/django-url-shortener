from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('short/<str:key>', views.redirect_link, name='redirect')
]

