from django.urls import path, include
from users.models import Users
from rest_framework import routers, serializers, viewsets
from .views import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer


# router = routers.DefaultRouter()
# # router.register(r'shop', ShopDetailsView,basename='')
# router.register(r'', UserViewSets)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('shop/<int:pk>/', ShopDetailsView.as_view()),
    ####------------- Front Page -------------#####
    path('Front/Phones/',FrontPhonesListView.as_view()),
    path('Front/Car/',FrontCarListView.as_view()),
    path('Front/others/',FrontotherListView.as_view()),
    ####-------------------Business Front Page-----------######
    path('Business/Phones/',BusinessPhonesListView.as_view()),
    path('Business/Car/',BusinessCarListView.as_view()),
    path('Business/others/',BusinessotherListView.as_view()),

    # path('api-auth/', include('rest_framework.urls'))
    path('post/',PostListView.as_view()),
    path('post/create/',PostCreateView.as_view()),
    path('post/det/<pk>',PostDetailView.as_view()),
    path('post/<pk>/update',PostUpdateView.as_view()),
    path('post/<pk>/delete',PostDeleteView.as_view()),


    path('Phones/',PhonesListView.as_view()),
    path('Phones/create/',PhonesCreateView.as_view()),
    path('Phones/det/<pk>',PhonesDetailView.as_view()),
    path('Phones/<pk>/update',PhonesUpdateView.as_view()),
    path('Phones/<pk>/delete',PhonesDeleteView.as_view()),

    path('order/',orderListView.as_view()),
    path('order/create/',orderCreateView.as_view()),
    path('order/det/<pk>',orderDetailView.as_view()),
    path('order/det/<pk>/update',orderUpdateView.as_view()),
    path('order/det/<pk>/delete',orderDeleteView.as_view()),

    path('Car/',CarListView.as_view()),
    path('Car/create/',CarCreateView.as_view()),
    path('Car/det/<pk>',CarDetailView.as_view()),
    path('Car/<pk>/update',CarUpdateView.as_view()),
    path('Car/<pk>/delete',CarDeleteView.as_view()),

    path('Catagoriess/',CatagoriessListView.as_view()),
    path('Catagoriess/create/',CatagoriessCreateView.as_view()),
    path('Catagoriess/det/<pk>',CatagoriessDetailView.as_view()),
    path('Catagoriess/det/<pk>/update',CatagoriessUpdateView.as_view()),
    path('Catagoriess/det/<pk>/delete',CatagoriessDeleteView.as_view()),

    path('Shop/',ShopListView.as_view()),
    path('Shop/create/',ShopCreateView.as_view()),
    path('Shop/det/<pk>',ShopDetailView.as_view()),
    path('Shop/<pk>/update',ShopUpdateView.as_view()),
    path('Shop/<pk>/delete',ShopDeleteView.as_view()),

    path('Profile/',ProfileListView.as_view()),
    path('Profile/create/',ProfileCreateView.as_view()),
    path('Profile/det/<pk>',ProfileDetailView.as_view()),
    path('Profile/det/<pk>/update',ProfileUpdateView.as_view()),
    path('Profile/det/<pk>/delete',ProfileDeleteView.as_view()),

    path('Review/',ReviewListView.as_view()),
    path('Review/create/',ReviewCreateView.as_view()),
    path('Review/det/<pk>',ReviewDetailView.as_view()),
    path('Review/det/<pk>/update',ReviewUpdateView.as_view()),
    path('Review/det/<pk>/delete',ReviewDeleteView.as_view()),
]
