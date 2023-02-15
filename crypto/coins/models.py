from django.db import models

# Create your models here.
class coin(models.Model):
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=50)
    price = models.FloatField(default=0, blank=True)
    rank = models.IntegerField(default=0, blank=True)
    image = models.CharField(blank=True, null=True,max_length=1000)

    def __str__(self):
        return str(self.name)
    
    class Meta:
        ordering = ['rank']