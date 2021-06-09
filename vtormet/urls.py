from django.urls import path
from .views import *


app_name = "vtormet"


urlpatterns = [
    path('', post_list, name='post_list_url'),
    path('recycling/', recycling, name='recycling_url'),
    path('create/', create_letter.as_view()),
    path('delete/<int:id>/', delete_letter.as_view()),
    path('raddet/<slug:raddet_category_slug>/', raddet_list, name='raddets')
]
