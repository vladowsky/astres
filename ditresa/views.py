from datetime import datetime
# from django.shortcuts import render
# from django.http import Http404
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.template import RequestContext
# from django.template import loader

from ditresa.models import Natal
from ditresa.forms import NatalForm, ReadNatalForm
from ditresa.utils import edit_permision, calc_level, level_calc_manager, \
                            user_session

# from django.utils import simplejson
import simplejson
import json

# Natal table 'Planet in the Zodiac' - from birthdate of the person 
# Sample natal table - read this table from database or from internet site
natal_tab_000 = {
            "Sun": "PIS",
            "Moo": "LIB",
            "Mer": "PIS",
            "Ven": "PIS",
            "Mar": "GEM",
            "Jup": "VIR",
            "Sat": "SAG",
            "Ura": "LEO",
            "Nep": "SCO",
            "Plu": "LEO"
            }

# Control table Zodiac-Planet for three es_levels
# Read this table from database, or from JSON file 
control_tab = {
            "ARI": ["Mar", "Mer", "Ura"],
            "TAU": ["Ven", "Vul", "Vul"],
            "GEM": ["Mer", "Ven", "Ear"],
            "CAN": ["Moo", "Nep", "Nep"],
            "LEO": ["Sun", "Sun", "Sun"],
            "VIR": ["Mer", "Moo", "Jup"],
            "LIB": ["Ven", "Ura", "Sat"],
            "SCO": ["Mar", "Mar", "Mer"],
            "SAG": ["Jup", "Ear", "Mar"],
            "CAP": ["Sat", "Sat", "Ven"],
            "AQU": ["Ura", "Jup", "Moo"],
            "PIS": ["Jup", "Plu", "Plu"]
} 

# Reference Planet-Symbol and Planet Lists tables 
# Reference tables - read this table from database or from JSON-files
planet_simbol = {"Sun": "☉", "Moo": "☽", "Mer": "☿", "Ven": "♀", "Mar": "♂", 
                 "Jup": "♃","Sat": "♄", "Ura": "♅", "Nep": "♆", "Plu": "♇", 
                 "Ear": "♁", "Vul": "V"}
planets12 = ["Sun", "Moo", "Mer", "Ven", "Mar", "Jup","Sat", "Ura", "Nep", 
             "Plu", "Ear", "Vul"]
planames12 = ["Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter","Saturn", 
              "Uran", "Neptun", "Pluto", "Earth", "Vulcan"]
planets10 = ["Sun", "Moo", "Mer", "Ven", "Mar", "Jup","Sat", "Ura", 
             "Nep", "Plu"]
planets = planets10


#----------------------------------------------------------------------
def index(request):
    """Index (home) page of the project"""
    context = {}
    pass
    context['username'] = user_session(request)
    return render(request, 'ditresa/index.html', context)  
    # return HttpResponse("You're visiting homepage of this project.")

#----------------------------------------------------------------------
def howto(request):
    """Describe how to draw astrograms, using this project tools"""
    context = {}
    pass
    context['username'] = user_session(request)
    return render(request, 'ditresa/howto.html', context)  
    # return HttpResponse("You're visiting homepage of this project.")


#----------------------------------------------------------------------
@login_required()
def graph(request, natal_id, esolevel):
    """View of the graph example"""
    # Initial tables for graph drawing
    context = {}
    if esolevel:
        esolevel = int(esolevel)
    else: 
        esolevel = 0

    instance = get_object_or_404(Natal, pk=natal_id)
    natal_tab = {
            "Sun": instance.sun,
            "Moo": instance.moon,
            "Mer": instance.mercury,
            "Ven": instance.venus,
            "Mar": instance.mars,
            "Jup": instance.jupiter,
            "Sat": instance.saturn,
            "Ura": instance.uran,
            "Nep": instance.neptun,
            "Plu": instance.pluto
            }

    # natal_tab = { k: natal_tab0[k][:3].upper() for k in natal_tab0 }

    print("natal_tab = ", natal_tab) 


    print(esolevel)
    # Calculations for graph output
    planets, planet_control, planet_level = level_calc_manager(natal_tab, 
                                        control_tab, esolevel, planets12)

    # print(' =============== Data output to JS ========================= ')
    # print('planets = ', planets)
    # print('planet_control = ', planet_control)
    # print('planet_level = ', planet_level)

    context['person'] = instance.person
    context['username'] = user_session(request)
    context['esolevel']       = esolevel
    context['natal_id']       = natal_id
    context['js_planet_simbol'] = json.dumps(planet_simbol)
    context['js_planets']       = json.dumps(planets)
    context['js_planet_control'] = json.dumps(planet_control)
    context['js_planet_level']  = json.dumps(planet_level)
   
    return render(request, 'ditresa/graph.html', context)  

#----------------------------------------------------------------------
@login_required()
def aslist(request):
    """View of the list of entries"""
    context = {}
    try:
        latest_entries_list = Natal.objects.order_by('-created_date')[:30]
        context = {'latest_entries_list': latest_entries_list}
        print(latest_entries_list[0].person)
    except IndexError:
        pass
    context['username'] = user_session(request)
    return render(request, 'ditresa/list.html', context)    

#----------------------------------------------------------------------
@login_required()
def new(request):
    """Add new entry"""
    context = {}
    context.update(csrf(request))
    user_id = request.user.id
    print('user_id = ', user_id)

    if request.method == 'POST': 
        form = NatalForm(request.POST)
        if form.is_valid(): 
            form.instance.user = request.user
            form.save() # сохранение  модели
            return HttpResponseRedirect('/astro/')
    else:
        form = NatalForm()

    user = user_session(request)

    context['username'] = user_session(request)
    context['planames12'] = planames12
    context['user_id'] = user_id
    # context['user'] = user_session(request)
    context['form'] = form
    return render(request, 'ditresa/new.html', context)


#----------------------------------------------------------------------
@login_required()
def edit(request, natal_id):
    """Entry editing"""
    context = {}
    context.update(csrf(request))
    instance = get_object_or_404(Natal, pk=natal_id)
    # instance = Natal.objects.get(whatever)
    if request.method == "POST":
        form = NatalForm(request.POST, instance=instance)
        if form.is_valid(): 
            form.instance.user = request.user
            form.save() # сохранение  модели
            return HttpResponseRedirect('/astro/')
    else:
        form = NatalForm(instance=instance)
    
    context['username'] = user_session(request)
    context['instance'] = instance
    context['natal_id'] = natal_id
    context['form'] = form
    return render(request, 'ditresa/edit.html', context)


#----------------------------------------------------------------------
@login_required()
def detail(request, natal_id):
    """Entry view"""
    context = {}
    esolevel = 0
    context.update(csrf(request))
    instance = get_object_or_404(Natal, pk=natal_id)
    form = ReadNatalForm(instance=instance)
    person = instance.person
    print(person)

    context['username'] = user_session(request)
    context['person'] = person
    context['esolevel'] = esolevel
    context['natal_id'] = natal_id
    context['planames12'] = planames12
    context['form'] = form
    context['instance'] = instance
    return render(request, 'ditresa/detail.html', context)

    

# #----------------------------------------------------------------------
@login_required()
def delete(request, natal_id):
    """ Delete the choosen sentence.
    """

    context = {}
    instance = get_object_or_404(Natal, pk=natal_id)
    Natal.objects.filter(id=natal_id).delete()

    context['instance'] = instance
    # context['username'] = user_session(request)
    
    return HttpResponseRedirect('/astro/')

#=================== Resistering and Login and Delete_account =============
def register(request, natal_id):
    ''' User registration view.
        Rendering and the processing input data.
    '''
    return HttpResponse("You're about to register in the project.")

#----------------------------------------------------------------------
def user_login(request):
    ''' Sign in of the user to the study environment ''' 
    context = {}
    context.update(csrf(request))
    
    if request.method == 'POST':    ## POST data from the login form.
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:        ## Mentioned user accound is valid.
            if user.is_active:      ## And the user account is active.
                login(request, user)
                request.session['username'] = username
                return HttpResponseRedirect('/astro/')
            else:                   ## Mentioned user accound is not active.
                context['disabled_account'] = True
                return render_to_response('ditresa/login.html', context)
        else:                       ## Mentioned user accound is not found.
            context['bad_details'] = True
            return render_to_response('ditresa/login.html', context)

    else:           ## Data is not HTTP POST (most likely be a HTTP GET).
        return render(request, 'ditresa/login.html', context)

#----------------------------------------------------------------------
@login_required()
def user_logout(request):
    ''' Logout of the login who is surely logged in ''' 
    if request.session.get('username'):
        ...
    logout(request)
    return HttpResponseRedirect('/astro/login/')






