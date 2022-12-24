from rest_framework import serializers
from Data import models


class YearSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Year
        exclude = ('CreatedBy', )


class ImportDatabaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ImportDatabase
        exclude = ('CreatedBy', )


class TradeInValueAddedSerializer(serializers.ModelSerializer):
    TiVAYears = YearSerializer(required=False, many=True)
    TiVADatabase = ImportDatabaseSerializer(required=False, many=True)

    class Meta:
        model = models.TradeInValueAdded
        exclude = ('Year', 'ImportDatabase',
                   'CreatedBy')
