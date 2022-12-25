from django.db import models

from core.base_items import models as base_models

from django.utils.translation import gettext_lazy as _

# Create your models here.
"""
This schema contains three models, Year, ImportDatabase and TradeInValueAdded.
ImportDatabase includes Year and Year includes TradeInValueAdded models.
                            

"""


class ImportDatabase(base_models.BaseModel):
    """ 
    This model is used to collect information regarding 
    the database that has been used to import the TiVA data.
    """
    DatabaseId = models.AutoField(
        _('Id'),
        primary_key=True
    )
    DatabaseName = models.CharField(
        _('Name of Database'),
        max_length=225,
        null=True,
        blank=True,
        default='',
    )
    IsActive = models.BooleanField(
        _('Is Active'),
        null=True,
        blank=True,
        default=True,
    )

    def save(self, force_insert=False, force_update=False):
        self.DatabaseName = self.DatabaseName.upper()
        return super(ImportDatabase, self).save(force_insert=force_insert, force_update=force_update)

    def __str__(self):
        return f"{self.DatabaseName} - {self.DatabaseId}"

    class Meta:
        verbose_name = _("Import Database")
        verbose_name_plural = _("Import Databases")
        db_table = "ImportDatabase"


class DatabaseYear(base_models.BaseModel):
    """ 
    This model is used to bind a specific year to a specific IO model
    """
    Year = models.IntegerField(
        _('Year'),
        primary_key=True,
    )
    IsAbnormal = models.BooleanField(
        _('Is the year abnormal'),
        null=True,
        blank=True,
        default=False,
    )
    ImportDatabase = models.ForeignKey(
        'Data.ImportDatabase',
        on_delete=models.CASCADE,
        related_name='DatabaseYears',
    )

    def __str__(self):
        return f"{self.Year} - {self.ImportDatabase}"

    class Meta:
        verbose_name = _('DatabaseYear')
        verbose_name_plural = _('DatabaseYears')
        db_table = 'DatabaseYear'


class TradeInValueAdded(base_models.BaseModel):
    """
    This model collects Trade In Value Added data from various sources and various years.
    Foreign key relation: many(TradeInValueAdded)-to-one(DatabaseYear)
    """
    TiVAId = models.BigAutoField(
        _('Id'),
        primary_key=True,
    )
    DatabaseYear = models.ForeignKey(
        "Data.DatabaseYear",
        on_delete=models.CASCADE,
        related_name="TiVAYears"
    )
    InputCountry = models.CharField(
        _('Input country'),
        max_length=50,
        null=True,
        blank=True,
        default=''
    )
    InputSector = models.CharField(
        _('Input Sector'),
        max_length=500,
        null=True,
        blank=True,
        default=''
    )
    OutputCountry = models.CharField(
        _('Output country'),
        max_length=50,
        null=True,
        blank=True,
        default=''
    )
    OutputSector = models.CharField(
        _('Output Sector'),
        max_length=500,
        null=True,
        blank=True,
        default=''
    )
    ValueAdded = models.FloatField(
        _('Trade in Value Added'),
        null=True,
        blank=True,
        default=0.0,
    )

    def __str__(self):
        return f"{self.InputCountry} - {self.InputSector} - {self.OutputCountry} - {self.OutputSector}"

    def save(self, force_insert=False, force_update=False):
        self.InputCountry = self.InputCountry.upper()
        self.InputSector = self.InputSector.upper()
        self.OutputCountry = self.OutputCountry.upper()
        self.OutputSector = self.OutputSector.upper()
        return super(TradeInValueAdded, self).save(force_insert=force_insert, force_update=force_update)

    class Meta:
        verbose_name = _('Trade in Value Added')
        verbose_name_plural = _('Trade in Values Added')
        db_table = "TradeInValueAdded"
