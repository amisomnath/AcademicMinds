from rest_framework import serializers
from school_management_system_api import models


class StudentSerializer(serializers.ModelSerializer):
    """Serializes a student object"""

    dob = serializers.DateField(format="%d/%m/%Y", input_formats=['%d/%m/%Y', 'iso-8601'])

    class Meta:
        model = models.Student
        fields = ('id', 'first_name', 'last_name', 'dob', 'address', 'phone')
