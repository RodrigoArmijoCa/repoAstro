# Generated by Django 4.1 on 2022-09-20 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repoAstro', '0003_prob_opti_lambdita_alter_algo_opti_descripcion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solucion',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='./images/'),
        ),
    ]