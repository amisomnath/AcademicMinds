from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from school_management_system_api.views import StudentViewSet, SubjectViewSet, TeacherViewSet, \
    StudentSubjectMappingViewSet, TeacherStudentMappingViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="SCHOOL MANAGEMENT SYSTEM API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="singha.somnath2@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('student/', StudentViewSet.as_view(), name='create-student'),
    path('subject/', SubjectViewSet.as_view(), name='create-subject'),
    path('teacher/', TeacherViewSet.as_view(), name='create-teacher'),
    path('enroll/student/<int:student_id>/subject/<int:subject_id>', StudentSubjectMappingViewSet.as_view(),
         name='enroll_student'),
    path('teachers/student/<int:student_id>', TeacherStudentMappingViewSet.as_view(), name='teachers-students'),

]
