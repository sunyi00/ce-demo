# -*- coding: utf-8

from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from flags.models import Flag
from foods.models import Food


def index(request):
    color_flag = Flag.objects.get(name='color')
    if color_flag:
        return HttpResponse(color_flag.status)
    else:
        return HttpResponse('white')

def foods(request):
    food_list = []
    for food in Food.objects.all():
        food_list.append({food.name: food.id})
    return JsonResponse({'foods': food_list})

def food_detail(request, foodid):
    return JsonResponse('')
