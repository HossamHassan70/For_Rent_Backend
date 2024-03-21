from django.contrib import admin


class RequestAdmin(admin.ModelAdmin):
    list_display = ('title','price', )
    search_fields = ['title']
	
    
admin.site.register(Request,RequestAdmin)
