from rest_framework import serializers


class BaseNestedSerializer(serializers.ModelSerializer):
    """
    To use this base serializer, you can create a specific serializer class 
    that extends the base class and defines the necessary meta options. For example:
    
    
    class PhoneNumber(models.Model):
        person = models.ForeignKey(Person, on_delete=models.CASCADE)
        number = models.CharField(max_length=20)

    class PhoneNumberSerializer(serializers.ModelSerializer):
        class Meta:
            model = PhoneNumber
            fields = ['id', 'number']


    class PersonSerializer(BaseNestedSerializer):
        phone_numbers = PhoneNumberSerializer(many=True, required=False)

        class Meta:
            model = Person
            fields = ['id', 'name', 'phone_numbers']
            nested_field_name = 'phone_numbers'
            nested_serializer = PhoneNumberSerializer
            parent_field_name = 'person'

    """

    def create(self, validated_data):
        nested_objects_data = validated_data.pop(
            self.Meta.nested_objects_field)
        instance = self.Meta.model.objects.create(**validated_data)
        for nested_object_data in nested_objects_data:
            nested_object_serializer_class = self.Meta.nested_object_serializer_class
            nested_object_serializer = nested_object_serializer_class(
                data=nested_object_data)
            nested_object_serializer.is_valid(raise_exception=True)
            nested_object_serializer.save(
                **{self.Meta.nested_object_parent_field: instance})
        return instance

    def update(self, instance, validated_data):
        nested_objects_data = validated_data.pop(
            self.Meta.nested_objects_field)
        nested_objects = (getattr(instance, self.Meta.nested_objects_field)
                          .all())
        nested_objects = list(nested_objects)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        for nested_object_data in nested_objects_data:
            nested_object = next(
                (x for x in nested_objects if x.id == nested_object_data['id']), None)
            if nested_object:
                nested_object_serializer_class = self.Meta.nested_object_serializer_class
                nested_object_serializer = nested_object_serializer_class(
                    nested_object, data=nested_object_data)
                nested_object_serializer.is_valid(raise_exception=True)
                nested_object_serializer.save()
                nested_objects.remove(nested_object)
            else:
                nested_object_serializer_class = self.Meta.nested_object_serializer_class
                nested_object_serializer = nested_object_serializer_class(
                    data=nested_object_data)
                nested_object_serializer.is_valid(raise_exception=True)
                nested_object_serializer.save(
                    **{self.Meta.nested_object_parent_field: instance})
        for nested_object in nested_objects:
            nested_object.delete()
        return instance
