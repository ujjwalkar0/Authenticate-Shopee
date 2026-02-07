"""
Service layer for products app.
Handles business logic separate from views.
"""
from products.models import Product
from users.models import Users
from business.models import Shop
from customer.models import Customer
from delivery.models import DeliveryAgent
from orders.models import Orders
from django.db.models import Sum, Count, Q
from django.db.models.functions import Coalesce


class UserContextService:
    """Service to handle user-specific context and data."""
    
    def __init__(self, user):
        self.user = user
        self._user_profile = None
    
    @property
    def user_profile(self):
        """Lazy load user profile."""
        if self._user_profile is None and self.user.is_authenticated:
            try:
                self._user_profile = Users.objects.get(id=self.user.id)
            except Users.DoesNotExist:
                self._user_profile = None
        return self._user_profile
    
    @property
    def user_type(self):
        """Get user type (Customer, Business, Delivery Boy)."""
        if self.user_profile:
            return self.user_profile.user_type
        return None
    
    def is_customer(self):
        return self.user_type == "Customer"
    
    def is_business(self):
        return self.user_type == "Business"
    
    def is_delivery(self):
        return self.user_type == "Delivery Boy"


class ShopService:
    """Service for shop-related operations."""
    
    @staticmethod
    def get_user_shop(user):
        """Get shop for a user if exists."""
        return Shop.objects.filter(user_id=user).first()
    
    @staticmethod
    def user_has_shop(user):
        """Check if user has a shop."""
        return Shop.objects.filter(user_id=user).exists()


class CustomerService:
    """Service for customer-related operations."""
    
    @staticmethod
    def get_customer(user):
        """Get customer profile for a user."""
        return Customer.objects.filter(name=user).first()
    
    @staticmethod
    def is_registered(user):
        """Check if user is registered as customer."""
        return Customer.objects.filter(name=user).exists()


class DeliveryService:
    """Service for delivery agent operations."""
    
    @staticmethod
    def get_delivery_agent(user):
        """Get delivery agent profile for a user."""
        return DeliveryAgent.objects.filter(user_id=user).first()
    
    @staticmethod
    def is_registered(user):
        """Check if user is registered as delivery agent."""
        return DeliveryAgent.objects.filter(user_id=user).exists()


class ProductService:
    """Service for product-related operations."""
    
    @staticmethod
    def get_all_products():
        """Get all products ordered by newest first."""
        return Product.objects.all().order_by('-id')
    
    @staticmethod
    def get_products_by_pin(pin_no):
        """Get products by PIN code."""
        return Product.objects.filter(Pin_No=pin_no).order_by('-id')
    
    @staticmethod
    def get_products_by_user(user):
        """Get products created by a specific user."""
        return Product.objects.filter(user_id=user).order_by('-id')


class HomePageService:
    """
    Service to prepare home page context based on user type.
    Orchestrates other services to build the complete context.
    """
    
    def __init__(self, request):
        self.request = request
        self.user = request.user
        self.user_context = UserContextService(self.user)
    
    def _build_base_url(self, path):
        """Build absolute URL with correct protocol."""
        protocol = "https" if self.request.is_secure() else "http"
        return f"{protocol}://{self.request.get_host()}{path}"
    
    def get_context(self):
        """Build complete context for home page."""
        context = {
            'product_list': ProductService.get_all_products(),
            'products': 'Product List',
        }
        
        if not self.user.is_authenticated:
            return context
        
        # Add authenticated user context
        context['shop_already_exist'] = ShopService.user_has_shop(self.user)
        
        if context['shop_already_exist']:
            shop = ShopService.get_user_shop(self.user)
            context['shop_id'] = shop.id if shop else None
        
        # Add user type specific context
        context['user_type'] = self.user_context.user_type
        
        if self.user_context.is_customer():
            context.update(self._get_customer_context())
        elif self.user_context.is_business():
            context.update(self._get_business_context())
        elif self.user_context.is_delivery():
            context.update(self._get_delivery_context())
        
        return context
    
    def _get_customer_context(self):
        """Get context specific to customer users."""
        customer = CustomerService.get_customer(self.user)
        context = {
            'customer_registered': CustomerService.is_registered(self.user),
            'products': 'Product List',
        }
        
        if customer:
            context['customer_id'] = customer.id
            context['product_list'] = ProductService.get_products_by_pin(customer.pin_no)
        
        return context
    
    def _get_business_context(self):
        """Get context specific to business users - Dashboard data."""
        context = {
            'product_list': ProductService.get_products_by_user(self.user),
            'products': 'Your Products',
        }
        
        # Get shop info
        shop = ShopService.get_user_shop(self.user)
        context['shop'] = shop
        
        # Get products for this user
        products = Product.objects.filter(user_id=self.user)
        context['total_products'] = products.count()
        
        if shop:
            # Get orders for this shop
            orders = Orders.objects.filter(shop=shop)
            context['total_orders'] = orders.count()
            context['pending_orders'] = orders.filter(is_accepted__isnull=True).count()
            context['accepted_orders'] = orders.filter(is_accepted=True).count()
            context['rejected_orders'] = orders.filter(is_accepted=False).count()
            
            # Calculate total revenue from accepted orders
            revenue = orders.filter(is_accepted=True).aggregate(
                total=Coalesce(Sum('product__price'), 0)
            )
            context['total_revenue'] = revenue['total']
            
            # Calculate acceptance rate
            completed_orders = context['accepted_orders'] + context['rejected_orders']
            if completed_orders > 0:
                context['acceptance_rate'] = round((context['accepted_orders'] / completed_orders) * 100)
            else:
                context['acceptance_rate'] = 0
            
            # Recent orders (last 5)
            context['recent_orders'] = orders.select_related(
                'customer', 'product', 'customer__name'
            ).order_by('-id')[:5]
            
            # Top selling products
            top_products = products.annotate(
                order_count=Count('orders', filter=Q(orders__is_accepted=True)),
                revenue=Coalesce(Sum('orders__product__price', filter=Q(orders__is_accepted=True)), 0)
            ).filter(order_count__gt=0).order_by('-order_count')[:5]
            context['top_products'] = top_products
        else:
            context['total_orders'] = 0
            context['pending_orders'] = 0
            context['accepted_orders'] = 0
            context['rejected_orders'] = 0
            context['total_revenue'] = 0
            context['acceptance_rate'] = 0
            context['recent_orders'] = []
            context['top_products'] = []
        
        # Low stock products (stock <= 5)
        context['low_stock_products'] = products.filter(stock__lte=5).order_by('stock')[:5]
        context['low_stock_count'] = products.filter(stock__lte=5).count()
        
        # Revenue trend (placeholder)
        context['revenue_trend'] = 12
        
        # Sales chart data (placeholder)
        context['sales_labels'] = "['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']"
        context['sales_data'] = "[0, 0, 0, 0, 0, 0, 0]"
        
        return context
    
    def _get_delivery_context(self):
        """Get context specific to delivery users."""
        agent = DeliveryService.get_delivery_agent(self.user)
        return {
            'product_list': None,
            'products': '',
            'hostname': self._build_base_url('/delivery/orders/'),
            'accept': self._build_base_url('/orders/accept/'),
            'deliveryagent_registered': DeliveryService.is_registered(self.user),
            'deliveryagent_id': agent.id if agent else None,
        }
