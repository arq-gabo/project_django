from django.contrib import admin

from order_management.models import Customer, Articles, Orders

# Register your models here.

admin.site.register(Customer)
admin.site.register(Articles)
admin.site.register(Orders)
