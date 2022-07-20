from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=150)
    addres = models.TextField()
    birth_date = models.DateField()                 ### COLOCAR NO PADRAO DIA/MES/ANO
    cpf = models.CharField(max_length=11, verbose_name='CPF')  ##VALIDAR CPF?
    phone_number = models.CharField(max_length=15)             #LABEL SOMENTE NUMERO
    disable = models.BooleanField(default=False)

    def __str__(self):
        return self.name