from django.urls import path
from .views import *


urlpatterns=[
    path('reg/',RegView.as_view(),name="reg"),
    path('log/',LogView.as_view(),name="log"),
    path('mhome/',HomeView.as_view(),name="h"),
    path('logout/',LogoutView.as_view(),name="lgout"),

]