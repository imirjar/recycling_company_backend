from django.urls import path
from .views import *

urlpatterns = [
    path('login/', dash.as_view())
    ]