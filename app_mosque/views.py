from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView



class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["about"] = About.objects.last()
        # context["services"] = Service.objects.filter(is_featured=True)
        
        return context

