from django.db import models
from django.contrib.auth.models import User , Group

# Create your models here.



class MyUser(models.Model):
	class Meta:
		permissions = (
			('ver_todos_usuarios','Ver todos os usuarios'),
			)

class Atividade(models.Model):
	nome = models.CharField(max_length=50)
	descricao = models.TextField(max_length=500)
	dataInicial = models.DateField()
	dataFinal = models.DateField()
	conclusao = models.BooleanField()
	fk_group = models.ForeignKey(Group)
	def __unicode__(self):
		return self.id_group
	
