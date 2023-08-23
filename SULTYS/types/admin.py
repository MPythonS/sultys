from django.contrib import admin
from models import JuiceTypes, JuiceFruits, JuiceVegetables, JuiceBerries


# Register your models here.
class JuiceTypesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'active',
    )
    list_filter = ('active',)
    search_fields = ('name',)
    ordering = ('name',)


class JuiceFruitsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'active',
    )
    list_filter = ('active',)
    search_fields = ('name',)
    ordering = ('name',)


class JuiceVegetablesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'active',
    )
    list_filter = ('active',)
    search_fields = ('name',)
    ordering = ('name',)


class JuiceBerriesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'active',
    )
    list_filter = ('active',)
    search_fields = ('name',)
    ordering = ('name',)


admin.site.register(JuiceTypes, JuiceTypesAdmin)
admin.site.register(JuiceFruits, JuiceFruitsAdmin)
admin.site.register(JuiceVegetables, JuiceVegetablesAdmin)
admin.site.register(JuiceBerries, JuiceBerriesAdmin)
