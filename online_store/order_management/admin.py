from django.contrib import admin

from order_management.models import Customer, Articles, Orders

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display=("name", "address", "phone")
    search_fields=("name", "phone")

class ArticlesAdmin(admin.ModelAdmin):
    list_filter=("section",)

class OrdersAdmin(admin.ModelAdmin):
    list_display=("number", "date")
    list_filter=("date",)
    date_hierarchy="date"

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Orders, OrdersAdmin)
