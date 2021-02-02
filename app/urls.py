from django.urls import path
from django.conf.urls.static import static 
from django.conf import settings 
from . import views
from .views import *#search,MyOrderView,notifications,order_successful,Orderview,UserRegisterView,UserEditView,ProfileView,profile_upload,AddCatagoryView,HomeView,UpdatePostView,DeletePostView,ArticleDetailView,AddPostView

urlpatterns = [
    # path('', views.home, name="home"),
    path('rest-auth/facebook', FacebookLogin.as_view(), name='fb_login'),
    path('',HomeView.as_view(), name="home"),
    path('notifications',notifications,name='notifications'),
    path('search',search,name='search'),
    path('order',Orderview.as_view(),name='order'),
    path('order_success',order_successful,name='order_success'),
    # path('',views.header,name='homes'),

    path('item/<int:pk>',ArticleDetailView.as_view(),name="article-details"),
    path('item/<int:pk>/<int:st>',ArticleDetailView.as_view(),name="article-details"),
    path('mobiles/<int:pk>',MobilesDetailView.as_view(),name="mobiles-details"),
    path('mobiles/<int:pk>/<int:st>',MobilesDetailView.as_view(),name="mobiles-details"),
    path('Cars/<int:pk>',CarDetailView.as_view(),name="car-details"),
    path('Cars/<int:pk>/<int:st>',CarDetailView.as_view(),name="car-details"),

    path('ML/Cars',CarTest.as_view(),name="car-ml"),
    path('ML/Cars/res',ml_result,name="car-ml-res"),


    path('orders/<int:pk>',MyOrderView.as_view(),name="order-details"),
    path('orders/',MyOrdersView.as_view(),name="my_orders"),

    path('add/Mobiles/',MobileAddView.as_view(),name="add_phone"),
    path('add/Cars/',CarAddView.as_view(),name="add_car"),
    path('add/<str:cats>/',AddPostView.as_view(),name="add_post"),

    path('sells/',SellsView.as_view(),name="sells"),


    path('item/edit/<int:pk>',UpdatePostView.as_view(),name="update"),
    path('item/<int:pk>/delete',DeletePostView.as_view(),name="delete"),

    path('phones/edit/<int:pk>',UpdateMobilesView.as_view(),name="mobile_update"),
    path('phones/<int:pk>/delete',DeleteMobilesView.as_view(),name="mobile_delete"),

    path('cars/edit/<int:pk>',UpdateCarView.as_view(),name="car_update"),
    path('cars/<int:pk>/delete',DeleteCarView.as_view(),name="car_delete"), #DeleteCarView

    path('shop/create',ShopCreateViews.as_view(),name="shop_create"),
    path('shop/update/<int:pk>',ShopUpdateView.as_view(),name="shop_update"),

    path('ip/create',IPCreateViews.as_view(),name="IP_create"),
    path('ip/update/<int:pk>',IPUpdateView.as_view(),name="IP_update"),

    path('catagory/',AddCatagoryView.as_view(),name="catagory"),
    # path('header/<int:pk>',AddHeaderView.as_view(),name="header"),
    path('catagory/<str:cats>/',CatagoryView,name="catagoryview"),
    path('upload-csv/', profile_upload, name="profile_upload"),
    path('profile/<int:pk>',ProfileView.as_view(),name="profile"),
    path('edit_profile/',UserEditView.as_view(),name="editProfile"),
    # path('register/',UserRegisterView.as_view(),name="register"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

