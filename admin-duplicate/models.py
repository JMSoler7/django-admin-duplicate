
from django.contrib import admin


class DuplicateAdminMixin(admin.ModelAdmin):

    def duplicate_event(self, request, queryset):
        for object in queryset:
            object.id = None
            object.save()

    actions = [duplicate_event]
    duplicate_event.short_description = "Duplicate selected items"
