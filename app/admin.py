from django.contrib import admin
from .models import *

# Register your models here.

class catadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

admin.site.register(category,catadmin)

class prodAdmin(admin.ModelAdmin):
    list_display=['name','slug','price','stock','img','avaiable']
    list_editable=['price','stock','img','avaiable']
    prepopulated_fields={'slug':('name',)}

admin.site.register(product,prodAdmin)

admin.site.register(cartlist)

admin.site.register(item)
