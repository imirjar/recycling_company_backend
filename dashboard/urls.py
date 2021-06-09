from django.contrib import admin
from django.urls import path, include
from .views import CooperationPage, ActCreate, ActEdit, ActList, ActListArchive, Profile, CreateAnswer, accept_req_answ, decline_req_answ
from django.conf import settings
from django.conf.urls.static import static


app_name = 'dashboard'

urlpatterns = [
    path('', CooperationPage.as_view(), name='dashboard'),
    path('act_create/', ActCreate.as_view(), name="act_create"),
    path('act_edit/<int:requisition_answer_id>', ActEdit.as_view(), name="act_edit"),
    path('act_list/', ActList.as_view(), name="act_list"),
    path('act_list_archive/', ActListArchive.as_view(), name="act_list_archive"),
    path('profile/', Profile.as_view(), name="profile"),
    path('create_answer/<int:requisition_id>', CreateAnswer.as_view(), name="create_answer"),
    path('accept/<int:id>', accept_req_answ, name="accept_req_answ"),
    path('decline/<int:id>', decline_req_answ, name="decline_req_answ"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
