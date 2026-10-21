from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView): # Class Bases Views - Inheritance (OOP)
    template_name = "pagesTemplates/home.html"