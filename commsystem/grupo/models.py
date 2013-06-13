from django.db import models

# Create your models here.

class Grupo(models.Model):
	nomeGrupo = models.CharField(max_length = 100)