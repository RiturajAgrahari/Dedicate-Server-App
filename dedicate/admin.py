from django.contrib import admin
from .models import DedicateServer

# Register your models here.


class DedicateServerAdmin(admin.ModelAdmin):
    list_display = ("id", "server_zip", )


admin.site.register(DedicateServer, DedicateServerAdmin)

