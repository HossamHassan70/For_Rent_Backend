from django.contrib import admin

from payment_api.models import Payment



class PaymentAdmin(admin.ModelAdmin):
    list_display = ('amount','user')
    search_fields = ['amount']
	
    
admin.site.register(Payment,PaymentAdmin)
