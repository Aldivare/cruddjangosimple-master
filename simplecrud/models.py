from django.db import models

class Crudsimple(models.Model):
    id = models.IntegerField()
    id = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=50)
    nip = models.IntegerField()
    divisi = models.CharField(max_length=50)
    alamat = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)

    class Meta:
        db_table = "simplecrud"


