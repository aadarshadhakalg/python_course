from django.contrib import admin
from . import models


class SocialMediaInline(admin.TabularInline):
    model = models.SocialMedia
    extra = 3

@admin.register(models.MyInformation)
class MyInformationAdmin(admin.ModelAdmin):
    inlines = [SocialMediaInline]


admin.site.register(models.SocialMedia)
admin.site.register(models.ContactMessage)