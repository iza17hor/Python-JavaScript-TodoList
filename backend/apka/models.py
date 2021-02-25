from django.db import models

class Dni(models.Model): 
    title = models.CharField(max_length=140) 
    detail = models.CharField(max_length=140)
    
    def __str__(self):
        return self.title 

    class Meta:
        ordering = ['title'] 


class Cele(models.Model):
    cele = models.CharField(max_length=200)
    check = models.BooleanField()
    dni = models.ForeignKey(Dni, on_delete=models.CASCADE)

    def __str__(self):
            return self.cele

    class Meta:
        ordering = ['cele']

