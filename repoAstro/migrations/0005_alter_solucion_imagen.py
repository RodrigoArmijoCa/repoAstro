# Generated by Django 4.1 on 2022-09-20 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repoAstro', '0004_alter_solucion_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solucion',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='repoAstro/images/'),
        ),
    ]
