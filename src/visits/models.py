from django.db import models

# Create your models here.
class PageVisit(models.Model):
  # el id se llena automaticamente
  # estar pendiente de que tipo es para que la DB sea optima
  # siempre usar el makemigrations y migration para cuando hagamos cambios en los modelos
  path = models.TextField(blank=True, null=True)
  timestamp = models.DateTimeField(auto_now_add=True)