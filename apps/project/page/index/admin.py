from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import ContactModel

@admin.register(ContactModel)
class ContactAdmin(ImportExportActionModelAdmin):
    readonly_fields = (
        'id',
        'created',
        'updated',
        'unique_id',
        'language'
    )