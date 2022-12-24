from django.contrib import admin

from Data import models
# Register your models here.


class TradeInValueAddedInline(admin.StackedInline):

    model = models.TradeInValueAdded
    list_display = ['ImportDatabase', 'InputCountry',
                    'InputSector', 'OutputCountry',
                    'OutputSector', 'ValueAdded',
                    ]


@admin.register(models.ImportDatabase)
class ImportDataBaseAdmin(admin.ModelAdmin):
    inlines = [TradeInValueAddedInline, ]


@admin.register(models.Year)
class YearAdmin(admin.ModelAdmin):
    inlines = [TradeInValueAddedInline, ]


@admin.register(models.TradeInValueAdded)
class TradeInValueAddedAdmin(admin.ModelAdmin):
    list_display = ['ImportDatabase', 'InputCountry',
                    'InputSector', 'OutputCountry',
                    'OutputSector', 'ValueAdded',
                    ]
