# Generated by Django 4.0.3 on 2022-03-22 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0003_rename_posts_curso'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='link',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
