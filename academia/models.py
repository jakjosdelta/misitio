from django.db import models
# Create your models here.

class EstadisticasProvincia(models.Model):
    num_ergresos_prov = models.IntegerField()
    nombre_prov = models.CharField(max_length = 200)
    region_prov = models.CharField(max_length = 200)
    estableciemientos_publicos_prov = models.IntegerField()
    establecimientos_privados_prov = models.IntegerField()
    anio = models.CharField(max_length = 4)

    def __unicode__(self):
        return self.num_ergresos_prov