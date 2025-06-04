from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'semester', 'user', 'date_posted', 'is_available')
    search_fields = ('name', 'description')
    list_filter = ('semester', 'user')
    readonly_fields = ('date_posted',)

admin.site.register(Item, ItemAdmin)