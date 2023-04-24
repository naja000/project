from django.urls import path
from.views import *


urlpatterns=[
    path('addmrk/',AddMark.as_view(),name="mark"),
    path('addstudent/',AddStudentMView.as_view(),name="addstudent"),
    path('viewStudent/',ViewStudentView.as_view(),name="viewStudent"),
    path('delstudent/<int:id>',StudentDeleteView.as_view(),name="delstu"),
    path('editstudent/<int:sid>',StudEditMView.as_view(),name="editstu"),

]    
