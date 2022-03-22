from datetime import datetime
from django.db import models
from django.db.models.fields import CharField

class Imagem(models.Model):
    img = models.ImageField(upload_to='img')

    def __str__(self) -> str:
        return self.img.url

class Curso(models.Model):
    titulo = CharField(max_length=100)
    descricao = CharField(max_length=150)
    imagens = models.ManyToManyField(Imagem)
    data = datetime.now()
    sobre = CharField(max_length=500)
    link = CharField(max_length=500)


    def __str__(self):
        return self.titulo