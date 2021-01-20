from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


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
    detail = RichTextField()
    add_time = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank = True)

    class Meta:
        verbose_name_plural = 'News'

    def save(self, *args, **kwargs):
        
        if self.slug == None:
            slug = slugify(self.title)
            has_slug = New.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.title) + '-' + str(count)
                has_slug = New.objects.filter(slug=slug).exists()
                
            self.slug = slug
            
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    


class Comment(models.Model):
    new = models.ForeignKey(New, related_name='mensaje', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    comment = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.comment

    
