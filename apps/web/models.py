from django.db import models

# Create your models here.

class Especialidades(models.Model):
    especialidad=models.CharField(blank="False",verbose_name="Especialidad: ",max_length=40);

    def __str__(self):
        return self.especialidad

class About(models.Model):
    name=models.CharField(verbose_name="Nombre: ",max_length=80)
    perfil=models.CharField(verbose_name="Perfil: ",max_length=50)
    imagen=models.FileField(upload_to="perfil",verbose_name="Imagen de Perfil: ")
    
    correo=models.EmailField(verbose_name="Correo Electrónico: ")
    telefono=models.CharField(verbose_name="Telefono: ", max_length=30)
    contenido=models.TextField(verbose_name="Acerca de mí");

    def __str__(self):
        return self.name
    
class Services(models.Model):
    servicios=models.CharField(max_length=150,verbose_name="Descripción: ");
    hacking=models.TextField(verbose_name="Hacking Ético: ");
    web = models.TextField(verbose_name="Desarrollo Web");
    software= models.TextField(verbose_name="Desarrollo de Sofware");
    videos=models.TextField(verbose_name="Edición de Videos: ")
    responsive = models.TextField(verbose_name="Diseño Responsive: ");
    bd= models.TextField(verbose_name="Bases de Datos");

    def __str__(self):
        return self.servicios

class Portafolio(models.Model):
    proyecto=models.CharField(max_length=50,verbose_name="Nombre del Proyecto: ")
    fecha=models.DateTimeField(auto_now_add=False,editable=True,verbose_name="Fecha de creación: ");
    categoria=models.ForeignKey(Especialidades,on_delete=True)
    imagen=models.ImageField(upload_to="portafolio",verbose_name="Imagen Descriptiva: ")

    def __str__(self):
        return  self.proyecto