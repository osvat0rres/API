from rest_framework import serializers
from .models import BookMenu

class BookMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookMenu
        fields = ['id', 'tittle', 'author','price', 'inventory']
        