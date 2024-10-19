from django.contrib import admin
from tms.models import Target, Vulnerability

class TargetAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'description', 'ip', 'hostname')

class VulnerabilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'description', 'category')

admin.site.register(Target, TargetAdmin)
admin.site.register(Vulnerability, VulnerabilityAdmin)
