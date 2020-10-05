from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)
    category_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class New(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    detail = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title

class Comment(models.Model):
    new = models.ForeignKey("New", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    comment = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.comment