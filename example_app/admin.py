from django.contrib import admin
from .models import Albums

class AlbumAdmin(admin.ModelAdmin):
    ...


admin.site.register(Albums, AlbumAdmin)
