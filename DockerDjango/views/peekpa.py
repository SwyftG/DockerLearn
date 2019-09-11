# encoding: utf-8
__author__ = 'lianggao'
__date__ = '2019/9/11 12:22 PM'

from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    context = {}
    context['hello_text'] = '「皮爷撸码」'
    return render(request, 'peekpa_index.html', context)