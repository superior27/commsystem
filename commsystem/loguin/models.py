from django.db import models
from django.contrib.auth.models import User , Group

# Create your models here.



class MyUser(models.Model):
	class Meta:
		permissions = (
			('ver_todos_usuarios','Ver todos os usuarios'),
			)

"""Apaguei o model anterior estava muito ruim"""
class Atividade(models.Model):
	dataInicial = models.DateField()
	horaInicial = models.TimeField()
	dataFinal = models.DateField()
	horaFinal = models.TimeField()
	titulo = models.CharField(max_length=100)
	descricao = models.TextField()
	grupo = models.ForeignKey(Group)

	def __unicode__(self):
		return u"%s - Inicio %s %s - Termino %s %s" %(self.titulo,self.dataInicial,self.horaInicial,self.dataFinal,self.horaFinal)
	
