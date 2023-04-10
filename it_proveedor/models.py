from django.db import models

class Empresas (models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    nit = models.CharField(max_length=50)
    nrc = models.CharField(max_length=50)
    pagina_web = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.nombre

class Suc_Empresa(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    empresa = models.ForeignKey(
        Empresas,
        verbose_name=("Empresa"), 
        related_name="Sucursal",
        on_delete=models.CASCADE
        )

    def __unicode__(self):
        return self.nombre

class Representante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    sucursal = models.ForeignKey(Suc_Empresa, on_delete=models.CASCADE)
    def __unicode__(self):
        return self.nombre

