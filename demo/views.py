# -*- coding: utf-8

from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


def index(request):
    return HttpResponse('demo index')

def foods(request):
    return JsonResponse('')

def food_detail(request, foodid):
    return JsonResponse('')
