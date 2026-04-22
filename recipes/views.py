from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .models import Recipe
# Create your views here.

class MainView(LoginRequiredMixin,View):
    def get(self,request):
        r=Recipe.objects.all()
        ctx={'recipe_list':r}
        return render(request,'recipes/recipe_list.html',ctx)
