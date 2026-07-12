from django.http import HttpResponse
from django.views import generic

def index(request):
    return HttpResponse("Hello, world.")

class Home(generic.TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["my_message"] = f"おはよう、{self.request.user.username}"
        return context