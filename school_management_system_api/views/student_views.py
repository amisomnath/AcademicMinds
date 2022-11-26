from django.db import transaction
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from school_management_system_api.models import Student
from school_management_system_api.serializers.student_serializers import StudentSerializer


class StudentViewSet(generics.CreateAPIView):
    """Handle view to create student details"""

    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = StudentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
