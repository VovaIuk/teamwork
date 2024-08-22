from django.contrib import admin

from main.models import Columns, Cards

@admin.register(Cards)
class CardsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Columns)
