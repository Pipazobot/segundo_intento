from django.db import models

class cuaderno(models.Model):
    materia = models.CharField(max_length=200)
    apuntes = models.TextField(null=True)
    puntuacion = models.IntegerField()
    def __str__(self):
        return 'f{self.materia}-holaa'
    
