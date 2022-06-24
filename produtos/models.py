from datetime import datetime
from django.db import models
from django.db.models.fields import CharField
from django.utils.safestring import mark_safe

class Imagem(models.Model):
    img = models.ImageField(upload_to='img')

    @mark_safe
    def icone(self):
        return f'<img width="30px" src="/media/{self.img}">'

    def __str__(self) -> str:
        return self.img.url

class Curso(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=150)
    imagens = models.ManyToManyField(Imagem)
    data = datetime.now()
    sobre = models.TextField(max_length=500)
    texto = models.TextField(max_length=2000)
    link = CharField(max_length=500)


    def __str__(self):
        return self.titulo