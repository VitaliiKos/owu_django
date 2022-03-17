from django.db import models


class ComputerModel(models.Model):
    class Meta:
        db_table = 'computers'
    brand = models.CharField(max_length=30)
    computer_model = models.CharField(max_length=30)
    memory_capacity = models.IntegerField()
    monitor = models.IntegerField()

    def __str__(self):
        return self.brand
