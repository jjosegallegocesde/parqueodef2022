from django.forms import modelform_factory
from django.shortcuts import render

from datetime import datetime

from web.models import Tiquetes,Celdas

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

