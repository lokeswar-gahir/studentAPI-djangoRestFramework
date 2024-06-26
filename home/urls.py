from django.urls import path
from .views import *

urlpatterns = [
    path("", Index.as_view(), name='home'),
    path("student-form/", StudentForm.as_view(), name='student-form'),
    path('student/detail/<int:pk>/',StudentDetail.as_view(), name='student-detail'),
    # path("add-student/", add_student, name='add_student'),
    path("student/", StudentAPI.as_view(), name="student")
]
