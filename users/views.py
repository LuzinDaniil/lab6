from django.shortcuts import render
from users.models import *
from users.models import Goods_Models
from django.views.generic import View



class Users(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'index.html', {'users': users})


class Goods(View):
    def get(self, request):
        goods = Goods_Models.objects.all()
        return render(request, 'goods.html', {'goods': goods})
