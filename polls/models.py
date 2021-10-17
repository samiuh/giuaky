from django.db import models

# Create your models here.


class Database(models.Model):
    img = models.ImageField(upload_to="anh")
    sanpham = models.TextField()
    gia = models.TextField()
