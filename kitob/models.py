from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=30)
    deck = models.TextField()
    author = models.CharField(max_length=20, blank=True, null= True)
    image = models.ImageField(upload_to="books-imges/",blank=True, null= True, default="default/book.jpg")
    price = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title










# Create your models here.
