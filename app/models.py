
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_Administrator = models.BooleanField(default=False)
    is_AssistantTeacher = models.BooleanField(default=False)
    is_RegularTeacher = models.BooleanField(default=False)
    is_Student = models.BooleanField(default=False)
    Male          =models.BooleanField(default=False)
    Female        = models.BooleanField(default=False)


class School(models.Model):
    SchoolName = models.CharField(max_length=200)
    City =  models.CharField(max_length=200)
    State =  models.CharField(max_length=200)

    def __str__(self):
        return self.SchoolName
    
   
    

class Class(models.Model):
    ClassName = models.CharField(max_length=200)
    school = models.ForeignKey(School, on_delete=models.CASCADE,related_name="class_school", null=True,blank=True)

    class Meta:
        unique_together = (('ClassName','school'),)
   
    def __str__(self):
        return self.ClassName


class Teacher(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE,related_name="teacher_school", null=True,blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,blank=True)
    class Meta:
        unique_together = (('school','user'),)

    def __str__(self):
        return self.user.username


class Student(models.Model):
    dob = models.DateField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE,related_name="student_school", null=True,blank=True)
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE,related_name="student_teacher", null=True,blank=True)
    studetclass= models.ForeignKey(Class, on_delete=models.CASCADE, related_name="student_class",null=True,blank=True)
     

    class Meta:
        unique_together = (('school','user','teacher'),)

    def __str__(self):
        return self.user.username







































 
 