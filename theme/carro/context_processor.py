from django.shortcuts import redirect
from .carro import Carro # 1 de 2

def importe_total_carro(request):
    carro = Carro(request) #soluccion de un compañero por error key carro 2 de 2
    total = 0
    #if request.user.is_authenticated:
    for key, value in request.session["carro"].items():
        total = total + float(value["precio"])

    return {"importe_total_carro":total}