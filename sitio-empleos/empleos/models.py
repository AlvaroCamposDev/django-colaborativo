from django.db import models

# Modelo para categorías de empleos
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Categorías"

# Modelo para ubicaciones de empleos
class Ubicacion(models.Model):
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100, default="Colombia")
    
    def __str__(self):
        return f"{self.ciudad}, {self.pais}"
    
    class Meta:
        verbose_name_plural = "Ubicaciones"

# Modelo principal para empleos
class Empleo(models.Model):
    # Opciones para tipo de empleo
    TIPO_CHOICES = [
        ('full-time', 'Tiempo Completo'),
        ('part-time', 'Medio Tiempo'),
        ('contract', 'Contrato'),
        ('remote', 'Remoto'),
    ]
    
    titulo = models.CharField(max_length=200)
    empresa = models.CharField(max_length=150)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    tipo_empleo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    salario_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salario_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    email_contacto = models.EmailField()
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.titulo} - {self.empresa}"
    
    class Meta:
        ordering = ['-created_at']  # Ordenar por más reciente primero