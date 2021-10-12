from django.db import models

# Create your models here.
class Contacto(models.Model):  
    cid = models.CharField(max_length=20)  
    cnombre = models.CharField(max_length=100)  
    capellidos = models.CharField(max_length=100)  
    cemail = models.EmailField()  
    etelefono = models.CharField(max_length=15)  
    class Meta:  
        db_table = "contacto"