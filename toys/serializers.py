from rest_framework import serializers
from .models import Toy


class ToySerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=150)
    description = serializers.CharField(max_length=250)
    toy_category = serializers.CharField(max_length=200)
    release_date = serializers.DateTimeField()
    was_included_in_home = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return Toy.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.toy_category = validated_data.get(
            'toy_category', instance.toy_category)
        instance.release_date = validated_data.get(
            'release_date', instance.release_date)
        instance.was_included_in_home = validated_data.get(
            'was_included_in_home', instance.was_included_in_home)
        instance.save()
        return instance


class ToyModelSerializer(serializers.ModelSerializer):
    """docstring for ToyModelSerializer"""

    class Meta:
        model = Toy
        fields = ('id', 'name', 'description', 'release_date',
                  'toy_category', 'was_included_in_home',)
