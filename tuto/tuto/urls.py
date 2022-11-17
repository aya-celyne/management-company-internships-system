"""tuto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Gestion.views import index, create,FormEns,FormEnt,FormProm,FormStage,AccesAdmin,ModifEtudiant,SuppEtudiant,SuppEns,ModifEns
from Gestion.views import ModifPrm,SuppPrm,ModifStage,SuppStage,ModifEnt,SuppEnt,FormGrp,SuppGrp,FormTypeStage,SuppTypeStage,ModifTypeStage
from Gestion.views import data_chart,Page1
urlpatterns = [
    path('admin/', admin.site.urls),

    path('index', index, name="index"),
    path('create', create , name="create"),
    path('ModifEtudiant/<str:pk>', ModifEtudiant , name="ModifEtudiant"),
    path('SuppEtudiant/<str:pk>',SuppEtudiant,name="SuppEtudiant"),

    path('FormGrp', FormGrp , name="FormGrp"),
    path('SuppGrp/<str:pk>', SuppGrp , name="SuppGrp"),

    path('FormEns', FormEns , name="FormEns"),
    path('SuppEns/<str:pk>',SuppEns,name="SuppEns"),
    path('ModifEns/<str:pk>',ModifEns,name="ModifEns"),

    path('FormEnt', FormEnt , name="FormEnt"),
    path('ModifEnt/<str:pk>',ModifEnt,name="ModifEnt"),
    path('SuppEnt/<str:pk>',SuppEnt,name="SuppEnt"),
  
    path('FormProm', FormProm , name="FormProm"),
     path('ModifPrm/<str:pk>',ModifPrm,name="ModifPrm"),
    path('SuppPrm/<str:pk>',SuppPrm,name="SuppPrm"),

    path('FormStage', FormStage , name="FormStage"),
    path('ModifStage/<str:pk>',ModifStage,name="ModifStage"),
    path('SuppStage/<str:pk>',SuppStage,name="SuppStage"),
    
    path('FormTypeStage', FormTypeStage , name="FormTypeStage"),
    path('ModifTypeStage/<str:pk>',ModifTypeStage,name="ModifTypeStage"),
    path('SuppTypeStage/<str:pk>',SuppTypeStage,name="SuppTypeStage"),
    
    path('', AccesAdmin , name="AccesAdmin"),
    
    path('data_chart', data_chart , name="data_chart"),

    path('Page1',Page1,name="Page1"),
]
