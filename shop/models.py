from django.db import models


# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField(max_length=12)
    # list_item = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Good'
        verbose_name_plural = 'Goods'

    def __str__(self):
        return f'{self.name} - {self.price}'


class Client(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    date_purchase = models.DateField()

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return f'{self.name} {self.age} {self.date_purchase}'


class Purchase(models.Model):
    objects = None
    detail_item = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Purchase'
        verbose_name_plural = 'Purchases'

    def __str__(self):
        return f'{self.detail_item}'
