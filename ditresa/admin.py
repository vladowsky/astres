from django.contrib import admin
from ditresa.models import Natal


class NatalAdmin(admin.ModelAdmin):
    pass
    fieldsets = [
    (None, {'fields': ['user', 'person', 'birth_date_time']}),
    ('Date information', {'fields': ['created_date'],'classes': ['collapse']})
    ]

    list_display = ('user', 'person', 'birth_date_time')

admin.site.register(Natal, NatalAdmin)

