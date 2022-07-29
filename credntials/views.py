## Crednetial app views

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from credntials import views
from django import template
from django.views.generic.base import View

# Create your views here.

def index(request):
    t1 = template.loader.get_template('credntials/index.html')
    html = t1.render()
    return HttpResponse(html)


def search_view(request):
    if "ser" in request.GET and  request.GET["ser"]:
        message = " You searched for %s" % request.GET['ser']
        return render(request, "credntials/index.html",{"message": message})
    else:
        return render(request, 'credntials/index.html', {"error": True} )


class CredntView(View):
    def get(self, request, *args, **kwargs):
        if "ser" in request.GET and request.GET["ser"]:
            message="ClassView  value is %s" % request.GET["ser"]
            RedirectView.as_view(url="http://localhost:8000")
        else:
            RedirectView.as_view(url="")
