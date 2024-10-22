from django.contrib import admin
from tms.models import Target, Vulnerability, Note

class TargetAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'description', 'ip', 'hostname')

class VulnerabilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'description', 'category')

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'content', 'linked_target')

admin.site.register(Target, TargetAdmin)
admin.site.register(Vulnerability, VulnerabilityAdmin)
admin.site.register(Note, NoteAdmin)
