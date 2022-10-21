from django.contrib import admin
from .models import car
from django.utils.html import format_html
# Register your models here.
class CarAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius:50px;" />'.format(object.car_photo.url))
    thumbnail.short_description="image"
    list_display=('car_title','thumbnail','model','year','fuel_type','is_feautered')
    list_display_links=('car_title','thumbnail')
    list_editable=('is_feautered',)
    search_fields=('car_title','model')
    list_filter=('model',)
admin.site.register(car,CarAdmin)
