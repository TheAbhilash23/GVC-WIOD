from django.contrib import admin

from Data import models
# Register your models here.


class TradeInValueAddedInline(admin.StackedInline):

    model = models.TradeInValueAdded
    list_display = ['DatabaseYear', 'InputCountry',
                    'InputSector', 'OutputCountry',
                    'OutputSector', 'ValueAdded',
                    ]


class DatabaseYearInline(admin.StackedInline):

    model = models.DatabaseYear
    list_display = ['Year', 'IsAbnormal',
                    'ImportDatabase',]

@admin.register(models.ImportDatabase)
class ImportDataBaseAdmin(admin.ModelAdmin):
    inlines = [DatabaseYearInline, ]


@admin.register(models.DatabaseYear)
class DatabaseYearAdmin(admin.ModelAdmin):
    inlines = [TradeInValueAddedInline, ]


@admin.register(models.TradeInValueAdded)
class TradeInValueAddedAdmin(admin.ModelAdmin):
    list_display = ['DatabaseYear', 'InputCountry',
                    'InputSector', 'OutputCountry',
                    'OutputSector', 'ValueAdded',
                    ]
