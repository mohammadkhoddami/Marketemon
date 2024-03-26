from django.contrib import admin
from .models import Category, Product
# Register your models here.

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'is_sub',)


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    raw_id_fields = ('category', )