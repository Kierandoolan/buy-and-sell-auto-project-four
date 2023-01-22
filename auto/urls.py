from . import views
from django.urls import path


urlpatterns = [
    path('', views.CarAdList.as_view(), name='home'),
    path('<slug:slug>/', views.AdDetail.as_view(), name='ad_detail'),
]
