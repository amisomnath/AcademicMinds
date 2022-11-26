from rest_framework import serializers
from school_management_system_api import models


class SubjectSerializer(serializers.ModelSerializer):
    """Serializes a subject object"""

    class Meta:
        model = models.Subject
        fields = ('id', 'subject_name', 'textbook')


class SubjectShortSerializer(serializers.ModelSerializer):
    """Serializes a subject short object"""

    class Meta:
        model = models.Subject
        fields = ('id',)
