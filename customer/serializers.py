from rest_framework import serializers
from .models import *


class UserNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNote
        fields= ['user','text_note']






       
