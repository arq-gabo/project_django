from django.contrib import admin

from order_management.models import Customer, Articles, Orders

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display=("name", "address", "phone")
    search_fields=("name", "phone")

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Articles)
admin.site.register(Orders)
