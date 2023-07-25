from django.db import models

# Create your models here.
class Propietario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.IntegerField()
    def _str_(self):
        return "%s" % (self.nombre)

class Edificio(models.Model):
    opciones_tipo_Edificio= (
        ('Residencial', 'Residencial'),
        ('Público', 'Público'),
        ('Negocio', 'Negocio'),
    )

    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30, \
        choices = opciones_tipo_Edificio)

    def _str_(self):
        return "%s %s %s %s" % (self.nombre,
                self.direccion,
                self.ciudad,
                self.tipo)
    
    
class Departamento(models.Model):
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, related_name='propietarios')
    costo = models.FloatField()
    num_cuartos = models.IntegerField()
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE,
            related_name="Departamentos")

    def _str_(self):
        return "%s %s %d %s" % (self.propietario,
                self.costo,
                self.num_cuartos,
                self.edificio)