from django.contrib import admin
from .models import Cvetmet, Raddet, Recycling, Raddet_category

# Register your models here.
@admin.register(Cvetmet)
class Cvetmet_Admin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name',)}
@admin.register(Raddet)
class RaddetAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category_id', 'opt', 'retail']
    list_editable = ['opt', 'retail']
    prepopulated_fields = {'slug': ('name',)}
@admin.register(Raddet_category)
class Raddet_CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
"""@admin.register(Recycling)
class RecyclingAdmin(admin.ModelAdmin):
    list_display = ['FkkoCode', 'FkkoDescription', 'collection', 'transportation', 'processing', 'disposal', 'utilization', 'placement']
    list_editable = ['collection', 'transportation', 'processing', 'disposal', 'utilization', 'placement']"""
##FkkoCode;FkkoDescription;collection;transportation;processing;disposal;utilization;placement
