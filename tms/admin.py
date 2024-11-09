from django.contrib import admin
from tms.models import Target, Vulnerability, Note, Ressource

class TargetAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'description', 'ip', 'hostname', 'status', 'type', 'last_update')

class VulnerabilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'description', 'category', 'cve')

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'content', 'linked_target')

class RessourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'description')

admin.site.register(Target, TargetAdmin)
admin.site.register(Vulnerability, VulnerabilityAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(Ressource, RessourceAdmin)
