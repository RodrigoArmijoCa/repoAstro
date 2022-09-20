# Generated by Django 4.1 on 2022-09-20 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repoAstro', '0002_solucion'),
    ]

    operations = [
        migrations.AddField(
            model_name='prob_opti',
            name='lambdita',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='algo_opti',
            name='descripcion',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='algo_opti',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='descripcion',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='prob_opti',
            name='descripcion',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='prob_opti',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
    ]