# -*- coding: utf-8 -*-
from django.db import models


class Tabelageral(models.Model):
    info_local = models.CharField(max_length=30)
    tipo_oco = models.CharField(max_length=30)
    def __unicode__(self):
       return "Local : %s  - Tipo de ocorrencia : %s "  % (self.info_local , self.tipo_oco)
  
class Tabelagrafico(models.Model):
    identificador = models.ForeignKey(Tabelageral)
    data = models.DateField()
    nun_oco = models.IntegerField()
    masc_infra = models.IntegerField()   
    masc_infra_morto = models.IntegerField()
    masc_vit = models.IntegerField()
    masc_vit_morto = models.IntegerField()
    fem_infra = models.IntegerField()   
    fem_infra_morto = models.IntegerField()
    fem_vit = models.IntegerField()
    fem_vit_morto = models.IntegerField()
    def __unicode__(self):
        return "Data : %s  - Identificador : %s "  % (self.data , self.identificador)