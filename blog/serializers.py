from rest_framework import serializers
from .models import *
#from rest_framework.parsers import JSONParser


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'description', 'image', 'sort_description']