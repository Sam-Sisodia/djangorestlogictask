from django.contrib import admin
from django.urls import path,include

from app import views
from rest_framework.routers import DefaultRouter



router = DefaultRouter()


router.register("User",views.Userdata, basename="Users" )

router.register("school",views.Schooldetails, basename="Schools" )
router.register("classes",views.Classdetaills, basename="class" )
router.register("teacher",views.teacherdetails, basename="teachers" )
router.register("student",views.Studentdetails, basename="students" )


urlpatterns = [
                
    path('crud/',include(router.urls)),
    path('sin/',views.SigleSchoolClassStudentlist.as_view()),
    path('studentslist',views.studentlist.as_view()),
    path('teacherlist',views.teacherlist.as_view()),

    
]