from django.contrib import admin

from requests_api.models import Request

class RequestAdmin(admin.ModelAdmin):
    list_display = ('title','price', )
    search_fields = ['title']
	
    
admin.site.register(Request,RequestAdmin)
