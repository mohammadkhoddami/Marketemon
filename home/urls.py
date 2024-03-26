from django.urls import path, include
from . import views
app_name = 'home'

#create bucket_urls for better management of our urls
bucket_urls = [

    path('', views.BucketHomeView.as_view(), name='bucket'),
    path('delete/object/<str:key>/', views.BucketDeleteObjectView.as_view(), name='bucket_delete_object'),
    path('download/object/<str:key>/', views.BucketDownloadObjectView.as_view(), name='bucket_download_object'),
]

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('category/<slug:category_slug>', views.HomePageView.as_view(), name = 'category'),
    path('bucket/', include(bucket_urls)),
    path('<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
]
