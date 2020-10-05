from django.db import models

# Create your models here.
class CategoryProductos(models.Model):
    name = models.CharField(max_length=300)
    featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

    class Meta: 

        db_table = 'Categories'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

class Product(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField()
    category = models.ForeignKey(CategoryProductos,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', blank=True)
    excerpt = models.TextField(max_length=200, verbose_name='Extracto')
    detail = models.TextField(max_length=1000, verbose_name='Información del producto')
    price = models.FloatField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'
        verbose_name = 'producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']
        