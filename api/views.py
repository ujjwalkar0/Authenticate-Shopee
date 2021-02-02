from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)
from rest_framework.views import APIView
from rest_framework import routers, serializers, viewsets,permissions
from app.models import *
from .serializers import *
# from rest_framework.response import Response
from django.http import JsonResponse


######--------Customer/Non-Logged User Front Page ---------#########
class UserViewSets(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializers

class FrontPhonesListView(ListAPIView):
    # queryset = Phones.objects.all()#[:10]
    # a = len(queryset)-8

    a=Phones.objects.all()
    l = a.count()-8
    queryset = a[l:]

    # queryset = queryset
    # try:
    #     queryset = queryset[a:10]
    # except:
    #     pass
    serializer_class = PhonesSerializer

class FrontCarListView(ListAPIView):
    b = Car.objects.all()
    try:
        queryset = b[len(b)-8:]
    except:
        queryset = b[8:]

    serializer_class = CarSerializer

class FrontotherListView(ListAPIView):
    c = Post.objects.all()
    try:
        queryset = c[len(c)-8:]
    except:
        queryset = c[8:]
    serializer_class = orderSerializer

#####----------------- Define Functions --------------#########

def get_objects_by_userid(Item,id):
    return Item.objects.filter(user_id=id.request.user.id)

def get_objects_by_pk(Item,pk):
    pass

# class ShopDetailsView(ListAPIView):
#     # queryset = Shop.objects.all()
#     serializer_class = ShopSerializer

#     # lookup_field = "id" #
#     # for i in queryset:
#     #     print(i.user_id)
#     def get_queryset(self,*args, **kwargs):
#         # for i in Shop.objects.all():#filter(user_id=self.kwargs['pk']):
#         print("Hi")
#         return Shop.objects.all() #filter(user_id=self.kwargs['pk'])
#         #  get_objects_by_userid(Phones,self)
#     print("\n")

#     def get(self, request, format=None):
#         return Response("test")
# class ShopDetailsView(ListAPIView):
#     serializer_class = ShopSerializer   
#     def get_queryset(self,*args, **kwargs):
#         return Shop.objects.filter(user_id=self.kwargs['pk'])

        # # print(Users.objects.filter(id=self.kwargs['pk']))
        # shop={}
        # for i in Shop.objects.filter(user_id=self.kwargs['pk']):
        #     shop['i.id']=i.id
        #     shop['i.user_id']=i.user_id
        #     shop['i.shop_name']=i.shop_name
        #     shop['i.address']=i.address
        #     shop['i.phone_no']=i.phone_no
        #     shop['i.email_id']=i.email_id
        #     shop['i.website']=i.website
        # #     print(QuerySet(i)[i.id-1])
        # print(shop)
        # return QuerySet({"_meta":1,"shop":shop})#Shop.objects.filter(user_id=self.kwargs['pk'])

#####-------------------Business Front Page-----------############

class BusinessPhonesListView(ListAPIView):
    serializer_class = PhonesSerializer
    def get_queryset(self,*args, **kwargs):
        return get_objects_by_userid(Phones,self)

class BusinessCarListView(ListAPIView):
    serializer_class = CarSerializer
    def get_queryset(self,*args, **kwargs):
        return get_objects_by_userid(Car,self)

class BusinessotherListView(ListAPIView):
    serializer_class = orderSerializer
    def get_queryset(self,*args, **kwargs):
        return get_objects_by_userid(Post,self)

######----------------  Profile View -------------------##########
# class ProfileView(generic.DetailView):
#     serializer_class = ProfileSerializer

#     def get_context_data(self, *args, **kwargs):
#         shop = Shop.objects.filter(user_id=self.kwargs['pk'])
#         context = super(ProfileView,self).get_context_data(*args, **kwargs)
#         context["shop"] = shop
#         return context

############-------------- Post ------------------##################
class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostCreateView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PostUpdateView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PostDeleteView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


############-------------- Phones ------------------##################
class PhonesListView(ListAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer
    paginate_by = 15

class PhonesDetailView(RetrieveAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer

class PhonesCreateView(CreateAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PhonesUpdateView(UpdateAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PhonesDeleteView(DestroyAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


############-------------- order ------------------##################
class orderListView(ListAPIView):
    queryset = order.objects.all()
    serializer_class = orderSerializer

class orderDetailView(RetrieveAPIView):
    queryset = order.objects.all()
    serializer_class = orderSerializer

class orderCreateView(CreateAPIView):
    queryset = order.objects.all()
    serializer_class = orderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class orderUpdateView(UpdateAPIView):
    queryset = order.objects.all()
    serializer_class = orderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class orderDeleteView(DestroyAPIView):
    queryset = order.objects.all()
    serializer_class = orderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


############-------------- Car ------------------##################
class CarListView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarDetailView(RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarCreateView(CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CarUpdateView(UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CarDeleteView(DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


############-------------- Catagoriess ------------------##################
class CatagoriessListView(ListAPIView):
    queryset = Catagoriess.objects.all()
    serializer_class = CatagoriessSerializer

class CatagoriessDetailView(RetrieveAPIView):
    queryset = Catagoriess.objects.all()
    serializer_class = CatagoriessSerializer

class CatagoriessCreateView(CreateAPIView):
    queryset = Catagoriess.objects.all()
    serializer_class = CatagoriessSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CatagoriessUpdateView(UpdateAPIView):
    queryset = Catagoriess.objects.all()
    serializer_class = CatagoriessSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CatagoriessDeleteView(DestroyAPIView):
    queryset = Catagoriess.objects.all()
    serializer_class = CatagoriessSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


###########--------------- Shop ----------#############

class ShopListView(ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

class ShopDetailView(RetrieveAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

class ShopCreateView(CreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ShopUpdateView(UpdateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ShopDeleteView(DestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    


############-------------- Profile ------------------##################
class ProfileListView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetailView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileCreateView(CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileUpdateView(UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDeleteView(DestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


############-------------- Review ------------------##################
class ReviewListView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetailView(RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewCreateView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewUpdateView(UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDeleteView(DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
