from django.contrib import admin
from .models import Cvetmet, Raddet, Recycling, Raddet_category, Customer, Requisition, RequisitionItem, RequisitionBid




@admin.register(Cvetmet)
class Cvetmet_Admin(admin.ModelAdmin):
    list_display = ['name', 'price', 'image']
    list_editable = ['price', 'image']


@admin.register(Raddet)
class RaddetAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'opt', 'retail', 'image']
    list_editable = ['opt', 'retail', 'image']


@admin.register(Raddet_category)
class Raddet_CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']
    

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'organization', 'email']
    prepopulated_fields = {"slug": ("organization",)}


@admin.register(Requisition)
class RequisitionAdmin(admin.ModelAdmin):
    list_display = ['number_in', 'number_out']


@admin.register(RequisitionItem)
class RequisitionItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'sap_material']

@admin.register(RequisitionBid)
class RequisitionBidAdmin(admin.ModelAdmin):
    list_display = ['customer', 'requisition', 'bid_sum']

