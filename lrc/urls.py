# this is the lrc appwide url config
#from django.conf.urls import urls
from lrc import views
from lrc.views import Lrcview
from django.urls import path, re_path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.index, name='home'),
    path("lrc/<int:indx>", views.indx_check, name='visit_pg' ),
    path('lrc1/', RedirectView.as_view(url="https://www.duckduckgo.com"), name='home'),
    path('time/', views.time_now, name='time_now'),
    path('lrc2/', views.index2, name = "index2"),
    path('lrc_view/', Lrcview.as_view(), name="lrcview" ),
]
