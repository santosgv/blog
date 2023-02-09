from django.contrib import admin
from .models import Curso, Imagem




@admin.register(Imagem)
class ImagemAdmin(admin.ModelAdmin):
    list_display =('icone',)

admin.site.register(Curso)