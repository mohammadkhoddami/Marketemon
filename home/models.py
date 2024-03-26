from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.


class Category(models.Model):
    sub_category = models.ForeignKey("self", on_delete=models.CASCADE, related_name='scategory', blank=True, null=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('name',)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("home:category", args=[self.slug])
    


class Product(models.Model):
    category = models.ManyToManyField(Category, related_name='pcategory')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField()
    description = RichTextField()
    price = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.category} - {self.slug}'

    def get_absolute_url(self):
        return reverse("home:product_detail", args=[self.slug,])
