from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.views.generic import ListView, TemplateView, DetailView, UpdateView
from .forms import StudentForm

def home(request):
    return render(request, 'index.html')

class Index(ListView):
    model=Student
    context_object_name = "students"
    template_name='index.html'
    
    def get_queryset(self):
        return super().get_queryset().order_by('-id')
class StudentForm(TemplateView):
    extra_context = {"form": StudentForm()}
    template_name='student_form.html'

class StudentDetail(UpdateView):
    template_name='student_detail.html'
    model= Student
    context_object_name = 'student'
    fields = ['image']
    # extra_context = {"form": StudentForm(instance=self.get_object())}
    
    # def get_context_data(self,*args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context['formss'] = StudentForm()
    #     return context
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["form"] = StudentForm()
    #     return context
    

# Create your views here.
# @api_view(['GET'])
# def home(request):
#     student_objs = Student.objects.all()
#     serializer = StudentSerializer(student_objs, many = True)
#     return Response({"status": 200, "message": "hello from django rest framework.", "data": serializer.data})

# @api_view(['POST'])
# def add_student(request):
#     new_student = request.data
#     serializer = StudentSerializer(data = new_student)
#     if not serializer.is_valid():
#         return Response({"status": 400, "message": "some error occured !!!", "erroes": serializer.errors})
#     serializer.save()
#     return Response({"status": 200, "message": "Data saved.", "data": new_student})

class StudentAPI(APIView):
    def get(self, request):
        try:
            student_id = request.GET.get("id")
            if student_id:
                student_obj = Student.objects.filter(id=student_id)
                if len(student_obj):
                    serializer = StudentSerializer(student_obj.first())
                    return Response({"status": 200, "message": "Data updated", "data": serializer.data})
                else:
                    return Response({"status": 200, "message": "student does not exist !!!", "data": None})
            else:
                student_objs = Student.objects.all()
                serializer = StudentSerializer(student_objs, many = True)
            return Response({"status": 200, "data": serializer.data})
        except Exception as e:
            print(e)
            return Response({"status": 500, "message": "some error occured !!!"})

    def post(self, request):
        try:
            new_student = request.data
            serializer = StudentSerializer(data = new_student)
            if not serializer.is_valid():
                # print(serializer.data)
                return Response({"status": 400, "message": "some error occured !!!", "errors": serializer.errors})
            serializer.save()
            return Response({"status": 200, "message": "Data saved", "data": serializer.data})
        except Exception as e:
            print(e)
            import logging
            log = logging.getLogger(__name__)
            log.exception('Any extra info you want to see in your logs')
            return Response({"status": 500, "message": "some error occured !!!"})

    
    def put(self, request):
        try:
            id = request.GET.get('id')
            student_obj = Student.objects.filter(id=id)
            if len(student_obj):
                serializer = StudentSerializer(student_obj.first(), data=request.data)
                if not serializer.is_valid():
                    return Response({"status": 400, "message": "some error occured !!!", "errors": serializer.errors})
                serializer.save()
                return Response({"status": 200, "message": "Data updated", "data": serializer.data})
            else:
                return Response({"status": 400, "message": "student does not exist !!!", "data": None})
        except Exception as e:
            print(e)
            return Response({"status": 500, "message": "some error occured !!!"})
    
    def patch(self, request):
        try:
            id = request.GET.get('id')
            student_obj = Student.objects.filter(id=id)
            if len(student_obj):
                serializer = StudentSerializer(student_obj.first(), data=request.data, partial=True)
                if not serializer.is_valid():
                    return Response({"status": 400, "message": "some error occured !!!", "errors": serializer.errors})
                serializer.save()
                return Response({"status": 200, "message": "Data updated", "data": serializer.data})
            else:
                return Response({"status": 400, "message": "Student does not exist !!!"})
        except Exception as e:
            print(e)
            return Response({"status": 500, "message": "some error occured !!!"})
        
    def delete(self, request):
        try:
            id = request.GET.get('id')
            student_obj = Student.objects.filter(id=id)
            if len(student_obj):
                serializer = StudentSerializer(student_obj.first())
                student_obj.first().delete()
                return Response({"status": 200, "message": "Student record Deleted", "data": serializer.data})
            else:
                return Response({"status": 400, "message": "Student does not exist !!!", "data": None})
        except Exception as e:
            print(e)
            return Response({"status": 500, "message": "some error occured !!!"})