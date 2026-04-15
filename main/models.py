from django.db import models
from datetime import  datetime

class Category(models.Model):
    name=models.CharField(max_length=110, unique=True)
    def __str__(self):
        return self.name
    def __repr__(self):
        return f"Pk: {self.pk}. Name {self.name}"
class News(models.Model):
    name=models.CharField(max_length=100)
    text=models.TextField()
    image = models.ImageField(upload_to='images/')
    views=models.IntegerField(default=0)
    created = models.DateTimeField(default=datetime.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    def __repr__(self):
        return f"Pk: {self.pk}. Name {self.name}"
