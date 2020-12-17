from rest_framework import serializers


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
