# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Tornado, TornadoDamage
from django.shortcuts import render

def tornado(request):
    all_tornado = Tornado.objects.all()  # Query all Tornado objects
    damage = TornadoDamage.objects.all()  # Query all TornadoDamage objects
    context = {'damage': damage, 'all_tornado': all_tornado}
    return render(request, 'tornado/nado.html', context)
