from datetime import datetime
from django.db import models
from django.db.models.fields import CharField



class Posts(models.Model):
    titulo = CharField(max_length=100)
    descricao = CharField(max_length=150)
    data = datetime.now()
    sobre = CharField(max_length=500)


    def __str__(self):
        return self.titulo