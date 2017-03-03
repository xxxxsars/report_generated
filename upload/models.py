from django.db import models

# Create your models here.
class Data(models.Model):
    Class = models.CharField(max_length=100)
    name  = models.CharField(max_length=100)
    num =  models.CharField(max_length=100)
    content = models.CharField(max_length=150)
    handle = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Second_Data(models.Model):
    Second_Class = models.CharField(max_length=100)
    Second_name  = models.CharField(max_length=100)
    Second_num  = models.CharField(max_length=100)
    Second_absenteeism = models.IntegerField()

    def __str__(self):
        return self.Second_name



class New_Second_Data(models.Model):
    Class = models.CharField(max_length=100)
    name  = models.CharField(max_length=100)
    num =  models.CharField(max_length=100)
    content = models.CharField(max_length=150)
    handle = models.CharField(max_length=100)

    def __str__(self):
        return self.N_name