from django.db import models

# Create your models here.
class estudiante(models.Model):
    id = models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=50, verbose_name="Nombre") #charfield = autoincremento
    apellido = models.CharField(max_length=50, verbose_name="Apellidos")
    foto = models.ImageField(upload_to='fotos/', verbose_name="Foto", null=True)
    clase = models.TextField(verbose_name="Clase", null=True)

    def __str__(self):
        fila = self.apellido + "  " + self.nombre
        return fila
    
    #borrar foto
    def delete(self, using=None, keep_parents=False):
        self.foto.storage.delete(self.foto.name)
        super().delete()