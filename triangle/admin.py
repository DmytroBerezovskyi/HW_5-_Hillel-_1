from django.contrib import admin  # noqa F401
from .models import LogModel, Person


# Register your models here.


class PersonAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    fieldsets = [
        ("Person", {"fields": (("first_name", "last_name"), "email"), "classes": ("wide", "extrapretty")}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    date_hierarchy = "pub_date"
    search_fields = ["first_name", "last_name"]
    search_help_text = "To search, enter the person's first or last name"


class LogAdmin(admin.ModelAdmin):
    list_display = ["request", "path", "date_time", "was_published_recently_log"]
    date_hierarchy = "date_time"


admin.site.register(Person, PersonAdmin)
admin.site.register(LogModel, LogAdmin)
