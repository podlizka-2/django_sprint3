from django.contrib import admin

from .models import Category, Location

admin.site.register(Category)
admin.site.register(Location)


class PostAdmin (admin.ModelAdmin):
    list_display = ('title', 'category', 'location', 'author', 'created_at')
    ist_filter = ('category', 'location', 'created_at')
    search_fields = ('title', 'content')
