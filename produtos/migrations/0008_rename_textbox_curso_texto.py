# Generated by Django 4.0.3 on 2022-03-26 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0007_alter_curso_descricao_alter_curso_sobre_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='textbox',
            new_name='texto',
        ),
    ]
