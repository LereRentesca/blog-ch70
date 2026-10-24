from django.views.generic import TemplateView
from django.shortcuts import HttpResponse, render

# Create your views here.
class HomePageView(TemplateView): # Class Based Views - Inheritance (OOP)
    template_name = "pagesTemplates/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['name'] = "Jack"
        print(context)
        return context


class AboutPageView(TemplateView):
    template_name = "pagesTemplates/about.html"

# Function Based Views
def contact_page(request):
    # print(request.__dict__)
    # return HttpResponse("Hello World from a FBV")

    contact_info = {
        "name": "Luis",
        "address": "Something 444, CA",
        "email": "lrenteria@sdgku.edu"
    }

    return render(request, "pagesTemplates/contact.html", contact_info)