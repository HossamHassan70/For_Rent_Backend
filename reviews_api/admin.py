from django.contrib import admin
from reviews_api.models import Review
# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    list_display = ( 'title','rating')
    search_fields = ['title','rating']
    list_filter = ['created_at']
	
    
admin.site.register(Review,ReviewAdmin)

