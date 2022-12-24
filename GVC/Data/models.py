from django.db import models
from core.base_items import models as base_models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Year(base_models.BaseModel):
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

    def __str__(self):
        return f"{self.Year} - {self.IsAbnormal}"

    class Meta:
        verbose_name = _('Year')
        verbose_name_plural = _('Years')
        db_table = 'Year'


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

    def save(self, force_insert=False, force_update=False):
        self.DatabaseName = self.DatabaseName.upper()
        return super(ImportDatabase, self).save(force_insert=force_insert, force_update=force_update)

    def __str__(self):
        return f"{self.DatabaseId} - {self.DatabaseName}"

    class Meta:
        verbose_name = _("Import Database")
        verbose_name_plural = _("Import Databases")
        db_table = "ImportDatabase"


class TradeInValueAdded(base_models.BaseModel):
    """
    This model collects Trade In Value Added data from various sources and various years.
    """
    IOId = models.BigAutoField(
        _('Id'),
        primary_key=True,
    )
    Year = models.ForeignKey(
        "Data.Year",
        on_delete=models.CASCADE,
        related_name="TiVAYears"
    )
    ImportDatabase = models.ForeignKey(
        "Data.ImportDatabase",
        on_delete=models.CASCADE,
        related_name="TiVADatabases"
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
