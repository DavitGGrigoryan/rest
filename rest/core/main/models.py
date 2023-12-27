from django.db import models

class Category(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    

class SubCategory(models.Model):

    category = models.ForeignKey(Category,      on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    

class Product(models.Model):

    category=models.ForeignKey(SubCategory,              on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
