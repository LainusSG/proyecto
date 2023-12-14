from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .utils import is_ajax, classify_face
import base64
from logs.models import Log
from django.core.files.base import ContentFile
from django.contrib.auth.models import User
from profiles.models import Profile

def login_view(request):
    return render(request, 'login.html', {})

def logout_view(request):
    logout(request)
    return redirect('/login')

def logint_view(request):
    return render(request, 'loginT.html', {})



@login_required

def home_view(request):
    return render(request, 'bienvenida.html', {})

#modulo 1 vistas-----
#----------------------------------------------------------
#----------------------------------------------------------
#----------------------------------------------------------
#----------------------------------------------------------
def find_user_view(request):
    if is_ajax(request):
        photo = request.POST.get('photo')
        _, str_img = photo.split(';base64')

        # print(photo)
        decoded_file = base64.b64decode(str_img)
        print(decoded_file)

        x = Log()
        x.photo.save('upload.png', ContentFile(decoded_file))
        x.save()

        res = classify_face(x.photo.path)
        if res:
            user_exists = User.objects.filter(username=res).exists()
            if user_exists:
                user = User.objects.get(username=res)
                profile = Profile.objects.get(user=user)
                x.profile = profile
                x.save()

                login(request, user)
                return JsonResponse({'success': True})
        return JsonResponse({'success': False})
    
#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------#
#------------------------ programacion de cirugia -----------------------------------#
#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------# 
def creacionP(request):
    return render(request, 'modulo1/creacion-de-paquetes.html', {})

def programacionC_view(request):
    return render(request, 'modulo1/programacion-de-cirugia.html', {})

def datosDC (request):
    return render (request,'modulo1/datos-de-cirugia.html', {} )


#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------#
#--------------------------------- recepcion ----------------------------------------#
#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------# 
def incidencias(request):
    return render(request, 'incidencias.html', {})

def materialdequirofano(request):
    return render(request, 'material-de-quirofano.html', {})

def otrasrecepciones(request):
    return render(request, 'otras-recepciones.html', {})

def otrasrecepciones2(request):
    return render(request, 'otras-recepciones2.html', {})

def otrasunidadeshospitalarias(request):
    return render(request, 'otras-unidades-hospitalarias.html', {})

def proveedorexterno(request):
    return render(request, 'proveedor-externo.html', {})

def recepciondeprovedorexterno(request):
    return render(request, 'recepcion-de-provedor-externo.html', {})

def recepcion(request):
    return render(request, 'recepcion.html', {})



#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------#
#----------------------------------- lavado -----------------------------------------#
#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------# 
def lavado(request):
    return render(request, 'lavado.html', {})

def lavadoopc2(request):
    return render(request, 'lavado-opc2.html', {})



#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------#
#----------------------------------- empaque ----------------------------------------#
#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------# 
def materialdequirofanoyCEYE(request):
    return render(request, 'material-de-quirofanoyCEYE.html', {})

def empaquetadoset(request):
    return render(request, 'empaquetado-set.html', {})

def otrasareasyproveedorexterno(request):
    return render(request, 'otras-areas-y-proveedor-externo.html', {})

def otrosempaquetados(request):
    return render(request, 'otros-empaquetados.html', {})

def lecturaQr(request):
    return render(request, 'lectura-de-qr.html', {})


#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------#
#------------------------------ esterilizacion --------------------------------------#
#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------# 
def contenidodeesterilizacion(request):
    return render(request, 'contenido-de-esterilizacion.html', {})

def esterilizacion2(request):
    return render(request, 'esterilizacion-2.html', {})

def esterilizacionno(request):
    return render(request, 'esterilizacion-no.html', {})

#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------#
#------------------------------------ almacen ---------------------------------------#
#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------# 
def almacengeneral(request):
    return render(request, 'almacen-general.html', {})

def recepciondealmacenamiento(request):
    return render(request, 'recepcion-de-almacenamiento.html', {})

#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------#
#-------------------------------- distribucion --------------------------------------#
#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------# 
def distribucionmaterialQx(request):
    return render(request, 'distribucion-materialQx.html', {})

def distribucionotros(request):
    return render(request, 'distribucion-otros.html', {})

def materialdequirofanodistribucion(request):
    return render(request, 'material-de-quirofano-distribucion.html', {})

def otrasareasyproveedorexternodistribucion(request):
    return render(request, 'otras-areas-y-proveedor-externo-distribucion.html', {})

def prestamosotros(request):
    return render(request, 'prestamos-otros.html', {})

#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------#
#------------------------------- administracion -------------------------------------#
#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------# 
def dashboard(request):
    return render(request, 'dashboard.html', {})

def altadeinstrumental(request):
    return render(request, 'alta-de-instrumental.html', {})

def controldeusuarios(request):
    return render(request, 'control-de-usuarios.html', {})

def datosdelavadoras(request):
    return render(request, 'datos-de-lavadoras.html', {})

def datosdelesterilizador(request):
    return render(request, 'datos-del-esterilizador.html', {})

def incidenciaadministrador(request):
    return render(request, 'incidencia-administrador.html', {})

def permisosdeusuarios(request):
    return render(request, 'permisos-de-usuarios.html', {})