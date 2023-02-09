from django.db import models
from django.db.models.fields import CharField


class Produto(models.Model):
    produto = CharField(max_length=100)
    descricao = CharField(max_length=150)
    imagens = models.ImageField(upload_to='img')
    link = CharField(max_length=150)


    def __str__(self):
        return self.produto