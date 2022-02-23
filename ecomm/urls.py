from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path("", views.base),
    
    path('', views.home, name='home'),
    path('signup/', views.signup),
    path('save/', views.save, name='save'),
    path('login/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order/',views.order_dtl, name='order'),
    path('js', views.js, name='js')

    ]
