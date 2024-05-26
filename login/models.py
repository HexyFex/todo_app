from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                             blank=True)  # on_delete definiert, wie sich die Datenbank verhalten soll, wenn ein referenzierter Datensatz gelöscht wird.
