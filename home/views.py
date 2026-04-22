from django.views import View
from django.shortcuts import render
from django.conf import settings

# Create your views here.

class HomeView(View):
    def get(self, request):
        is_local = settings.DEBUG
        context = {'installed': settings.INSTALLED_APPS, 'is_local': is_local}
        return render(request, 'home', context)
"""
class HomeView(View):
    def get(self,request):
        host=request.get_host()
        islocal=host.find('localhost')>=0 or host.find('127.0.0.1')>=0
        context={'installed':settings.INSTALLED_APPS,'islocal':islocal}
        return render(request,'home/main.html',context)"""

