from django.contrib import admin
from .models import Performer, Requisition, Answer, RequisitionAnswer
# Register your models here.

@admin.register(Performer)
class Performer_Admin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Requisition)
class Requisition_Admin(admin.ModelAdmin):
    list_display = ['number']

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(RequisitionAnswer)
class RequisitionAnswer_Admin(admin.ModelAdmin):
    list_display = ['requisition', 'performer', ]
