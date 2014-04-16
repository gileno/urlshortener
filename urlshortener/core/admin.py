from django.contrib import admin

from .models import Link


class LinkAdmin(admin.ModelAdmin):

    list_display = ['url', 'slug', 'views', 'created_at', 'updated_at']
    search_fields = ['slug', 'url']
    list_filter = ['created_at', 'updated_at']


admin.site.register(Link, LinkAdmin)
