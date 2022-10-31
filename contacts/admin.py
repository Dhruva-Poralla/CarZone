from django.contrib import admin
from .models import contact
# Register your models here.
class contactAdmin(admin.ModelAdmin):
    list_display=('id','first_name','last_name','car_title','email','created_date')
    list_display_links=('first_name','email')
    search_fields=('first_name','last_name','car_title')


admin.site.register(contact,contactAdmin)
