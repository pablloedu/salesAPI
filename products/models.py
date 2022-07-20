from django.db import models

# Create your models here.
class Product(models.Model):

    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=6,decimal_places=2) # FLOAT FIELD TA ESTRANHO
    brand = models.CharField(max_length=150)
    description = models.TextField()
#SETOR DO PRODUTO////////ESTOQUE???
    disable = models.BooleanField(default=False)

    def __str__(self):
        return self.name
