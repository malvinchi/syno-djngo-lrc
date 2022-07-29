from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from django import template
from django.views.generic.base import View
from django.views.generic.base import RedirectView

import datetime

# Create your views here.
def index(request):
    t = template.loader.get_template('lrc/homepage.html')
    html = t.render()
    return HttpResponse(html)

def indx_check(request, indx):
    if indx == 1:
        return index1(request, indx)
    elif indx == 2:
        return index2(request, indx)
    else:
        return HttpResponse("this page does not exist")

def time_now(request):
    now=datetime.datetime.now()
    html ='<html><body> The time now is {0} </body></html>'.format(now)
    return HttpResponse(html)


def index1(request, indx):
    time_now(request)
    # host = request.get_host()
    return HttpResponse("<h2>Welcome to Lrc 1.! </h2> <br/> <h4> Information about Accessed URL(this url) of django</h4> <br/> Path:  {}. <br> Complete Path: {}. <br/>Security: {}. <br/> Hostname: {} <br/> UserReferrer: {} <br/> Remote Address: {}".format(request.path, request.get_full_path(), request.is_secure(), request.get_host(), request.META["HTTP_USER_AGENT"], request.META["REMOTE_ADDR"]))

def index2(request, indx):
    values = request.META.items()

    html = []
    for x, y in values:
        html.append("<tr><td> %s </td> :  <td> %s </td></tr>" % (x, y))

    return HttpResponse("<table> %s </table>" % '\n'.join(html))


class Lrcview(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("First View Class Response")
