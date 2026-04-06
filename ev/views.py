# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from decimal import Decimal
from tornado.models import Tornado

# Custom JSON Encoder to handle Decimal objects
class DecimalEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)  # or float(obj)
        return super(DecimalEncoder, self).default(obj)

def index(request):
    # Fetch latest entries from each model
    latest_quake = Earthquake.objects.latest('date')
    latest_tsunami = Tsunami.objects.latest('date')
    latest_eruption = VolcanicEruption.objects.latest('year')
    latest_tornado = Tornado.objects.latest('date')  # Fetch latest tornado entry

    context = {
        'latest_quake': latest_quake,
        'latest_tsunami': latest_tsunami,
        'latest_eruption': latest_eruption,
        'latest_tornado': latest_tornado,  # Include latest tornado entry
    }
    return render(request, 'etv/home.html', context)

def quakes(request):
    all_quakes = Earthquake.objects.all()
    damage = EarthquakeDamage.objects.all()
    context = {'all_quakes': all_quakes, 'damage': damage}
    return render(request, 'etv/quake.html', context)

def tsunami(request):
    all_tsunami = Tsunami.objects.all()
    damage = TsunamiDamage.objects.all()
    context = {'all_tsunami': all_tsunami, 'damage': damage}
    return render(request, 'etv/tsunami.html', context)

def volcano(request):
    all_eruptions = VolcanicEruption.objects.all()
    damage = VolcanoDamage.objects.all()
    context = {'all_eruptions': all_eruptions, 'damage': damage}
    return render(request, 'etv/volcano.html', context)
