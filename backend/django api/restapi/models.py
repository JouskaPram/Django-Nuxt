from django.db import models

class Category(models.Model):
    kategori = models.CharField(max_length=100)
    deskripsi = models.TextField()
  
class Product(models.Model):
    nama = models.CharField(max_length=50)
    price = models.IntegerField()
    id_category = models.ForeignKey(Category,on_delete=models.CASCADE)

