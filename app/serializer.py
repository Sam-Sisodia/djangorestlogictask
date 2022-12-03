from . models import *
from rest_framework import serializers








class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id','SchoolName','City','State']




class ClassSerializers(serializers.ModelSerializer):
  
    class Meta:
        model = Class
        fields = ["id","ClassName",'school']

        #depth =1



class UserSerlizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','is_Administrator','is_AssistantTeacher','is_RegularTeacher','is_Student','Male',
                               'Female']



class Teacherserializer(serializers.ModelSerializer):
    user = UserSerlizer()
    class Meta:
        model = Teacher
        fields = ['id','school','user',]


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerlizer()
    school = SchoolSerializer()
    teacher =Teacherserializer()
    studetclass = ClassSerializers()
    class Meta:
        model = Student
        fields = "__all__"


class Studentcrudserilizer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class TeacherCrud(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id','school','user',]






