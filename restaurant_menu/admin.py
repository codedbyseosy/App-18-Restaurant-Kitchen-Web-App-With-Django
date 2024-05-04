from django.contrib import admin
from .models import Item

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("meal", "status")
    list_filter = ("status",) # filter by status to check if meal is available
    search_fields = ("meal", "description") # search fields by meal or description


admin.site.register(Item, MenuItemAdmin)