from django.db import models
import os
import datetime

def get_file_path_foto( instance, filename):
    ext = os.path.splitext(filename)[1]
    filename = "%s%s" % (instance.nip, ext)
    return os.path.join('images/', filename)

class Crudsimple(models.Model):
    nip = models.IntegerField(primary_key=True, null=False, blank=False)
    nama = models.CharField(max_length=50)
    foto = models.ImageField(upload_to=get_file_path_foto, null=True, blank=True)
    divisi = models.CharField(max_length=50)
    alamat = models.CharField(max_length=50)
    gender_choices = (
        ('Pria', 'Pria'),
        ('Wanita', 'Wanita'),
    )
    gender = models.CharField(max_length=50, null=False, choices=gender_choices)
    test = models.Choices

    def __str__(self):
        return str(self.nip)

    class Meta:
        db_table = "simplecrud"


