from orders.models import Orders
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import *
from delivery.models import DeliveryAgent, Accepted
from delivery.forms import DeliveryAgentForm
from users.models import Users

class OrdersView(APIView):
    def post(self, request, *args, **kwargs):
        hostname = f"http://{self.request.get_host()}/"
        if self.request.is_secure():
            hostname = f"https://{self.request.get_host()}/"

        data = list()
        order = Orders.objects.filter(pin_no=request.data)
        for i in order:
            if not i.is_accepted:
                data.append({
                    "customer_name": i.customer.name.first_name +" "+ i.customer.name.last_name,
                    "customer_phone_no": i.customer.phone_no,
                    "customer_address": i.customer.address,
                    "shop_name": i.shop.shop_name,
                    "shop_address": i.shop.address,
                    "shop_contact_number": i.shop.phone_no,
                    "product_name": i.product.title,
                    "product_image": f"{hostname}media/"+str(i.product.image1),
                    "order_id": i.id
                })
        # print(data)
        return Response(data)
    
class NewAgent(CreateView):
    model = DeliveryAgent
    form_class = DeliveryAgentForm
    template_name = "delivery/create.html"
    success_url = "/"

    def form_valid(self, form):
        user = Users.objects.get(username=self.request.user)
        form.instance.user_id = user
        return super().form_valid(form)

class UpdateAgent(UpdateView):
    model = DeliveryAgent
    form_class = DeliveryAgentForm
    template_name = "delivery/create.html"
    success_url = "/"

    def form_valid(self, form):
        user = Users.objects.get(username=self.request.user)
        form.instance.user_id = user
        return super().form_valid(form)

class OrderedItemsView(ListView):
    model = Accepted
    template_name = "delivery/items.html"

    def get_context_data(self, *args ,**kwargs):
        context = super(OrderedItemsView, self).get_context_data(*args, **kwargs)

        hostname = f"http://{self.request.get_host()}/"
        if self.request.is_secure():
            hostname = f"https://{self.request.get_host()}/"

        context["hostname"] = hostname

        return context
