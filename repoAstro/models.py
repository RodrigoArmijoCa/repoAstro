from django.db import models

class Dataset(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)

class Algo_opti(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)

class Prob_opti(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    lambdita = models.FloatField(null=True, blank=True)

class Solucion(models.Model):
    id_dataset = models.ForeignKey(Dataset, null=True, blank=True, on_delete=models.CASCADE)
    id_algo_opti = models.ForeignKey(Algo_opti, null=True, blank=True, on_delete=models.CASCADE)
    id_prob_opti = models.ForeignKey(Prob_opti, null=True, blank=True, on_delete=models.CASCADE)
    cant_ite = models.CharField(max_length=30)
    solucion_inicial = models.CharField(max_length=1000)
    solucion_final = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to='repoAstro/images/', null=True, blank=True)