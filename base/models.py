from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) # on_delete definiert, wie sich die Datenbank verhalten soll, wenn ein referenzierter Datensatz gelöscht wird.
    title = models.CharField(null=True, blank=True, max_length=200)
    description = models.TextField(null=True, blank=True, max_length=500)
    complete = models.BooleanField(default=False, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']