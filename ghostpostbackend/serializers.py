from rest_framework import serializers

from ghostpostbackend.models import BoastRoastModel


class BoastRoastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BoastRoastModel
        fields = '__all__'
