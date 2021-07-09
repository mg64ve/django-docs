from django.contrib import admin

from docs.models import doc

@admin.register(doc)
class docAdmin(admin.ModelAdmin):
    pass
