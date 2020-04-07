from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('account/', include('allauth.urls')),
    path('',views.index),
    path('/',views.index)
]