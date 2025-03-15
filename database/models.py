from django.db import models

class Calculation(models.Model):
    expression = models.CharField(max_length=255) 
    result = models.CharField(max_length=255)   


    def __str__(self):
        return f"{self.expression} = {self.result}"