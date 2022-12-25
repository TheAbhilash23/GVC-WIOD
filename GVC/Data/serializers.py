from rest_framework import serializers

from core.base_items import serializers as base_serializers
from Data import models


class TradeInValueAddedSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TradeInValueAdded
        exclude = ('CreatedBy', 'DatabaseYear')


class DatabaseYearSerializer(base_serializers.BaseNestedSerializer):
    TiVAYears = TradeInValueAddedSerializer(required=False, many=True)

    class Meta:
        model = models.DatabaseYear
        exclude = ('CreatedBy', 'ImportDatabase')
        nested_field_name = 'DatabaseYear'
        nested_serializer = TradeInValueAddedSerializer
        parent_field_name = 'Year'


class ImportDatabaseSerializer(base_serializers.BaseNestedSerializer):
    DatabaseYears = DatabaseYearSerializer(required=False, many=True)

    class Meta:
        model = models.ImportDatabase
        exclude = ('CreatedBy', )
        nested_field_name = 'ImportDatabase'
        nested_serializer = DatabaseYearSerializer
        parent_field_name = 'DatabaseId'
