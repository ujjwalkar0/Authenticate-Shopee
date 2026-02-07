"""
Views for the home app.
"""
from django.views.generic import ListView
from products.models import Product
from home.services import HomePageService


class HomeView(ListView):
    """
    Home page view - displays products based on user type.
    Business logic delegated to HomePageService.
    """
    model = Product
    template_name = "home/index.html"
    ordering = ['-id']
    paginate_by = 15

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        
        service = HomePageService(self.request)
        context.update(service.get_context())
        
        return context
