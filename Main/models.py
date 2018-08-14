from django.db import models

# Modelo de configuracion basica para la app movil.
class Configuration(models.Model):
    
    name=models.CharField(max_length=200)
    motto=models.CharField(max_length=200)
    logo=models.ImageField(upload_to='photos')
    mission=models.TextField(max_length=500)
    vision=models.TextField(max_length=500)
    info=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name