# -*- coding: utf-8 -*-
from django.views.generic import CreateView, ListView,TemplateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from grafico.models import *








def home(request):
    return render(request, 'home.html')


class Criar(CreateView):
    template_name = 'contato.html'
    model = Tabelagrafico
    success_url = reverse_lazy('grafico')

class Cadastrogeral(CreateView):
    template_name = 'cadastrogeral.html'
    model = Tabelageral
    success_url = reverse_lazy('grafico')



class Grafico(ListView):
    template_name = 'grafico.html'
    model =  Tabelagrafico
    paginate_by = None
    

    
class Grafico2(ListView):
     

 def post(self,request , *args, **kwargs):
        busca = request.POST['q']
        resultado = Tabelageral.objects.filter(info_local__contains = busca)
        return render(request,'grafico2.html',{'resultado' : info_local , 'resposta': True})
    
    
