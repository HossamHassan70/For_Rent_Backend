from django.contrib import admin

# Register your models here.
from property_api.models import Property


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'address')
    search_fields = ['title','address']
    list_filter = ['type']
	
    
admin.site.register(Property,PropertyAdmin)
