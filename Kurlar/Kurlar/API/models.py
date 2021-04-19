from django.db import models


class Kurlar(models.Model):
    doviz_ismi = models.CharField(max_length=10)
    alis = models.FloatField()
    satis = models.FloatField()
    fark = models.FloatField()
    kur_kodu = models.CharField(max_length=10)


    def __str__(self):
        return self.doviz_ismi
