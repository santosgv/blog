# Generated by Django 4.0.3 on 2022-03-22 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0004_curso_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='img')),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='imagens',
            field=models.ManyToManyField(to='produtos.imagem'),
        ),
    ]
