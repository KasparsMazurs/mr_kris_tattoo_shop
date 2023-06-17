from django.contrib import admin
from .models import Gallery
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    """
    Create an admin panel for Gallery
    """
    list_display = ('description', 'slug', 'body_part')
    prepopulated_fields = {'slug': ('description',)}
    fieldsets = (
        (None, {
            'fields': ('image','description', 'slug', 'body_part')
        }),
    )
