from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Grupo(models.Model):
	nomeGrupo = models.CharField(max_length = 30)
	def __unicode__(self):
		return self.nomeGrupo


class Grupo_Usuario(models.Model):
	id_grupo = models.ForeignKey(Grupo)
	id_usuario= models.ForeignKey(User)
	def __unicode__(self):
		return self.id_grupo

class Permissao_Grupo(models.Model):
	grupo = models.ForeignKey(Grupo)
	criar_grupo = models.BooleanField()
	deletar_grupo = models.BooleanField()
	alterar_grupo = models.BooleanField()
	criar_usuario = models.BooleanField()
	deletar_usuario = models.BooleanField()
	alterar_usuario = models.BooleanField()
	criar_atividade = models.BooleanField()
	deletar_atividade = models.BooleanField()
	alterar_atividade = models.BooleanField()
	def __unicode__(self):
		return self.criar_usuario


