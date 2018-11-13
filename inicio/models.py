from django.db import models

estado = (
	('contendiente','Contendiente'),
	('retador','Retador'),
	('campeon','Campeon'),
	('leyenda','Leyenda'),
)

suscripcion = (
	('normal','Normal'),
	('sincomerciales','5 Merciales'),
	('ilimitado','Ilimitado'),
	('premium','Premium'),
)

usuario = (
	('1','Registrado'),
	('2','Administrador'),
)

# Create your models here.
class Persona(models.Model):
	nombre 		= models.CharField(max_length = 150)
	email 		= models.EmailField()
	rut			= models.CharField(max_length = 15)
	nacimiento	= models.DateField()
	region		= models.CharField(max_length = 50)
	comuna		= models.CharField(max_length = 50)
	telefono	= models.CharField(max_length = 15)
	suscripcion	= models.CharField(max_length = 50, choices = suscripcion, default='normal')
	contrasena	= models.CharField(max_length = 30)
	usuario		= models.CharField(max_length = 50, choices = usuario, default='1')

	def __str__(self):
		return self.nombre


class Luchador(models.Model):
	imagen 		= models.ImageField(default='default.png', blank=True)
	nombre 		= models.CharField(max_length = 100)
	peleas		= models.CharField(max_length = 10)
	biografia	= models.CharField(max_length = 300)
	estado		= models.CharField(max_length = 50, choices = estado, default='contendiente')
	pertenece	= models.CharField(max_length = 30)
	contador	= models.CharField(max_length = 15, default=0)

	def __str__(self):
		return self.nombre
