from django.shortcuts import render
from django.views import View
from . import models
# Create your views here.


class Demo(View):
    def get(self, request):
        sanpham = models.Database.objects.all()
        return render(request, 'index.html', {"sp": sanpham})
