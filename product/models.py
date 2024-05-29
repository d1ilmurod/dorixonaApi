from django.db import models

# Create your models here.

class Kinds(models.Model):
    kind = models.CharField(max_length=50)

    def __str__(self):
        return self.kind


class Product(models.Model):
    title = models.CharField(max_length=50)
    about = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='product_image')
    knds_id = models.ForeignKey(Kinds,on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


