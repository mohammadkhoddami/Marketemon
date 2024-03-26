from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Product, Category
from . import tasks
from django.contrib import messages
from utils import AdminRequiredMixin
from orders.forms import CartAdd
# Create your views here.


class HomePageView(View):
    def get(self, request, category_slug=None):
        products = Product.objects.filter(available=True)
        categories = Category.objects.filter(is_sub=False)
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            products = products.filter(category=category)
        return render(request, 'home/index.html', {'products': products, 'categories': categories})


class ProductDetailView(View):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        form = CartAdd()
        return render(request, 'home/product.html', {'product': product, 'form': form})


class BucketHomeView(AdminRequiredMixin, View):
    temp = 'home/bucket.html'

    def get(self, request):
        objects = tasks.all_bucket_objects_task()
        return render(request, self.temp, {'objects': objects})


class BucketDeleteObjectView(AdminRequiredMixin, View):
    def get(self, request, key):
        tasks.delete_object_task.delay(key)
        messages.info(request, 'Your Object will be deleted soon', 'info')
        return redirect('home:bucket')


class BucketDownloadObjectView(AdminRequiredMixin, View):
    def get(self, request, key):
        tasks.download_object_task.delay(key)
        messages.info(request, 'Your Object Will Be Downlaod Soon', 'info')
        return redirect('home:bucket')
