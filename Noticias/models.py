from django.db import models

# Create your models here.
class Noticia(models.Model):
	idNoti = models.AutoField(primary_key = True)
	titulo = models.CharField(max_length = 30)
	textoNoti =  models.TextField(max_length = 500)
	fecha = models.DateField(auto_now = False)
	foto = models.ImageField(upload_to='/tmp')

	def __str__(self):
		return self.titulo