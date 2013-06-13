from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class MyUser(models.Model):
	class Meta:
		permissions = (
			('ver_todos_usuarios','Ver todos os usuarios'),
			)

