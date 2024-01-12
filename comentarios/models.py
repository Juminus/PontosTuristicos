from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Comentario(models.Model):
    usuario = models.ForeignKey(User)
    comentario = models.TextField()