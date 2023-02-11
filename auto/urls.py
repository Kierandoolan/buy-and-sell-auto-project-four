from . import views
from django.urls import path


urlpatterns = [
    path('', views.Home, name='home'),
    path('carlist', views.CarAdList.as_view(), name='carlist'),
    path('add_car/', views.AddCar, name='add_car'),
    path('contact/', views.contact_view, name='contact'),
    path('delete-car/<slug:slug>', views.DeleteCar, name='delete_car'),
    path('edit-car/<slug:slug>', views.EditCar, name='edit_car'),
    path('like/<slug:slug>', views.AdLike.as_view(), name='post_like'),
    path('<slug:slug>/', views.CarAdDetail.as_view(), name='Car_ad_detail'),
    path('delete_comment/<int:comment_id>',
         views.delete_comment, name='delete_comment'),
    
]
