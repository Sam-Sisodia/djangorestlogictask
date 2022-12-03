from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from . serializer import *
from . models import *
from rest_framework.generics import ListCreateAPIView

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.decorators import action

class Userdata(ModelViewSet):
    queryset=User.objects.values()
    serializer_class = UserSerlizer



class Schooldetails(ModelViewSet):
    queryset= School.objects.all()
    serializer_class= SchoolSerializer
    lookup_field = "id"

    @action(detail=True,methods = ["GET"])
    def schoolclass(self,request,id=None):
        clas = self.get_object()
      
        classs = Class.objects.filter(school_id=clas)
        serializer = ClassSerializers(classs,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @action(detail=True,methods = ["GET"])
    def teachers(self,request,id=None):
        tobj = self.get_object()
        objs = Teacher.objects.filter(school_id=tobj)
        teacherslist= []
        for i in objs:
            teacherslist.append(i.user_id)
        hh= User.objects.filter(id__in = teacherslist,)
        serializer = UserSerlizer(hh,many=True)
        return Response( serializer.data, status=status.HTTP_200_OK)


    @action(detail=True,methods = ["GET"])
    def students(self,request,id=None):
        tobj = self.get_object()
        objs = Student.objects.filter(school_id=tobj)
      
        studentlist=[]
        for i in objs:
            studentlist.append(i.user_id)
        
        student= User.objects.filter(id__in = studentlist)
      
        serializer = UserSerlizer(student,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    

    @action(detail=True,methods = ["GET"],)
    def sigleschoolclass(self,request,id=None):
        clas = self.get_object()
        print("==============", clas)
        cls_id= clas.id
        print("This is ----------------",cls_id)
        clasid = Class.objects.get(id = cls_id)
        serializer = ClassSerializers(clasid)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
        
       
        # print("This is ----------------",clas_id)
        # school = Class.objects.get(id=cls_id)
        # serializer = ClassSerializers(school)
        # return Response(serializer.data, status=status.HTTP_200_OK)
   



   

class Classdetaills(ModelViewSet):
    queryset= Class.objects.all()
    serializer_class= ClassSerializers
    lookup_field = "id"


    @action(detail=True,methods = ["GET"])
    def students(self,request,id=None):
        tobj = self.get_object()
        objs = Student.objects.filter(studetclass_id=tobj.id)
        print("THis i-------------------------------s objds",objs)
    

        student= User.objects.filter(id__in= objs
        )
        print("Students=======================", student)
        serializer = UserSerlizer(student,many=True)
       
        return Response(serializer.data, status=status.HTTP_200_OK)

    

class teacherdetails(ModelViewSet):
    queryset=Teacher.objects.all()
    serializer_class = TeacherCrud
    lookup_field = "id"



class Studentdetails(ModelViewSet):
    queryset=Student.objects.all()    
    serializer_class = Studentcrudserilizer



class studentlist(APIView):
    def get(self,request,):
        data =Student.objects.all()
        serializer = StudentSerializer(data,many=True)
        return Response(serializer.data)



class teacherlist(APIView):
    def get(self,request,):
        data =Teacher.objects.all()
        serializer = Teacherserializer(data,many=True)
        return Response(serializer.data)




















