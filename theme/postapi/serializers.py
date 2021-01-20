from rest_framework import serializers
from orbital.models import New

class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ('id', 'category', 'image', 'title', 'detail')