from django.db import models

class summa(models.Model):
    title=models.CharField(max_length=100)
    dis=models.CharField(max_length=250)
    ima=models.ImageField(upload_to='generator/images/')
    def __str__(self):
        return self.title 
