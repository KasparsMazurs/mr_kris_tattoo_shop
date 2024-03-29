from django.contrib import admin
from .models import Product
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    """
    Create an admin panel for Products
    """
    list_display = ('name', 'created_on')
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('description',)
    fieldsets = (
        (None, {
            'fields': ('image', 'name','slug', 
                       'description', 'product_price', 
                       'digital_product_price', 'product_type', )
        }),
    )
