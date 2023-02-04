from . import views
from django.urls import path


urlpatterns = [
    path('', views.Home, name='home'),
    path('carlist', views.CarAdList.as_view(), name='carlist'),
    path('add_car/', views.AddCar, name='add_car'),
    path('delete-car/<slug:slug>', views.DeleteCar, name='delete_car'),
    path('about', views.About, name='about'),
    path('like/<slug:slug>', views.AdLike.as_view(), name='post_like'),
    path('<slug:slug>/', views.CarAdDetail.as_view(), name='Car_ad_detail'),
    
    
]
