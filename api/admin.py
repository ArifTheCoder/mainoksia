from django.contrib import admin
from .models import Company, Week, Image

# Register your models here.
admin.site.register(Company)


class ImageInline(admin.StackedInline):
    model = Image
    extra = 1


@admin.register(Week)
class WeekAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

