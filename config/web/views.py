from django.forms import modelform_factory
from django.shortcuts import render

from datetime import datetime

from web.models import Tiquetes,Celdas,Tarifas

# Create your views here.
def Home(request):

    TiquetesFormulario=modelform_factory(Tiquetes,exclude=['fecha_salida','fecha_ingreso','valor_pagado'])
    formulario=TiquetesFormulario()

    tiquetes=Tiquetes.objects.all()

    data={
        'formulario':formulario,
        'tiquetes':tiquetes
    }

    if(request.method=='POST'):
        formEnvio=TiquetesFormulario(request.POST)
        if formEnvio.is_valid():
            datos=formEnvio.save(commit=False)
            datos.fecha_ingreso=datetime.now()
            datos.valor_pagado=0
            datos.save()

    return render(request,'index.html',data)


def CeldasVista(request):

    return render(request,'celdas.html')



def TarifasVista(request):

    return render(request,'tarifas.html')



def gestionarSalida(request,id):

    tiquete=Tiquetes.objects.get(pk=id)

    fechaInicio=tiquete.fecha_ingreso
    fechaSalida=datetime.now()
    diferencia=fechaSalida-fechaInicio.replace(tzinfo=None) 
    durationEnSegundos = diferencia.total_seconds() 
    duracionEnMinutos=int(durationEnSegundos/60)

    costo=duracionEnMinutos*150
   
    datos={
        'id':id,
        'tiquete':tiquete
    }

    if(request.method=='GET'):
        Tiquetes.objects.filter(pk=id).update(fecha_salida=datetime.now())
        Tiquetes.objects.filter(pk=id).update(valor_pagado=costo)
        

    return render(request,'salida.html',datos)