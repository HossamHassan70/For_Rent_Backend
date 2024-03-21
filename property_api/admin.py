from django.contrib import admin

# Register your models here.
from property_api.models import Property


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'type')
    search_fields = ['title','type']
	
    
admin.site.register(Property,PropertyAdmin)
