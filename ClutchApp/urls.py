from django.urls import path, include


from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login),
    path('loginuser', views.loginuser),
    path('index', views.index),
    path('addItem', views.addItem),
    path('imageInfo/<int:id>', views.itemInfo),
    path('editItem/<int:id>', views.editItem),
    path('addImage/<int:id>', views.addImage),
    path('gallery', views.gallery),
    path('contact', views.contact),
    path('FAQ', views.FAQ),
    path('gallery/<int:id>', views.galleryView),
    path('addGallery', views.addGallery),
    path('gadgets', views.gadgets),
    path('checkout', views.checkout),
    path('process_order', views.processOrder),
    path('emailList', views.emailList)
]