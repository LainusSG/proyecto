"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    login_view,
    logout_view,
    home_view,
    find_user_view,
    logint_view,
    
    #-------------------modulo 1--------------------
    programacionC_view,
    datosDC,
    creacionP,
    
    #-------------------recepción--------------------
    incidencias,
    materialdequirofano,
    otrasrecepciones,
    otrasrecepciones2,
    otrasunidadeshospitalarias,
    proveedorexterno,
    recepciondeprovedorexterno,
    recepcion,
    #----------------------------------- lavado -----------------------------------------#
    lavado,
    lavadoopc2,

    #----------------------------------- empaque ----------------------------------------#
    empaquetadoset,
    lecturaQr,
    materialdequirofanoyCEYE,
    otrasareasyproveedorexterno,
    otrosempaquetados,
    #------------------------------ esterilizacion --------------------------------------#

    #------------------------------------ almacen ---------------------------------------#

    #-------------------------------- distribucion --------------------------------------#

    #------------------------------- administracion -------------------------------------#


)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('login/', logint_view, name='loguint'),
    path('reconocimiento-facial/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('classify/', find_user_view, name='classify'),

    #-------------------modulo 1--------------------
    path ('programacion-de-cirugia/', programacionC_view, name='programacionC'),
    path ('creacion-de-paquetes/', creacionP, name='programacionC'),
    path ('datos-de-programacion/', datosDC, name='programacionC'),

     #-------------------recepción--------------------
     path ('incidencias/', incidencias, name='incidencias'),
     path ('material-de-quirofano/', materialdequirofano, name='material-de-quirofano'),
     path ('otras-recepciones/', otrasrecepciones, name='otras-recepciones'),
     path ('otras-recepciones2/', otrasrecepciones2, name='otras-recepciones'),
     path ('otras-unidades-hospitalarias/', otrasunidadeshospitalarias, name='otras-unidades-hospitalarias'),
     path ('proveedor-externo/', proveedorexterno, name='proveedor-externo'),
     path ('recepcion-de-provedor-externo/', recepciondeprovedorexterno, name='recepcion-de-provedor-externo'),
     path ('recepcion/', recepcion, name='recepcion'),
    #----------------------------------- lavado -----------------------------------------#
    path ('lavado/', lavado, name='lavado'),
    path ('lavado-opc2/', lavadoopc2, name='lavado-opc2'),

    #----------------------------------- empaque ----------------------------------------#
    path ('empaquetado-set/', empaquetadoset, name='empaquetado-set'),
    path ('lectura-de-qr/', lecturaQr, name='lectura-de-qr'),
    path ('material-de-quirofanoyCEYE/', materialdequirofanoyCEYE, name='material-de-quirofanoyCEYE'),
    path ('otras-areas-y-proveedor-externo/', otrasareasyproveedorexterno, name='otras-areas-y-proveedor-externo'),
    path ('otros-empaquetados/', otrosempaquetados, name='otros-empaquetados'),
    
    #------------------------------ esterilizacion --------------------------------------#
    path ('/', , name=''),
    path ('/', , name=''),
    path ('/', , name=''),
    path ('/', , name=''),
    path ('/', , name=''),
    path ('/', , name=''),
    path ('/', , name=''),
    path ('/', , name=''),
    
    #------------------------------------ almacen ---------------------------------------#
    path ('/', , name=''),
    path ('/', , name=''),
    path ('/', , name=''),
    path ('/', , name=''),
    path ('/', , name=''),
    path ('/', , name=''),
    path ('/', , name=''),
    path ('/', , name=''),

    #-------------------------------- distribucion --------------------------------------#
    path ('/', , name=''),
    path ('/', , name=''),
    path ('/', , name=''),
    path ('/', , name=''),
    path ('/', , name=''),
    path ('/', , name=''),
    path ('/', , name=''),
    path ('/', , name=''),

    #------------------------------- administracion -------------------------------------#
    path ('/', , name=''),
    path ('/', , name=''),
    path ('/', , name=''),
    path ('/', , name=''),
    path ('/', , name=''),
    path ('/', , name=''),
    path ('/', , name=''),
    path ('/', , name=''),




]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
