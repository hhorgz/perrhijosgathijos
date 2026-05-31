from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .models import Profile

def index(request):
    latest_profile_list = Profile.objects.order_by('-pub_date')[:5]
    template = loader.get_template('pets/index.html')
    context = {'latest_profile_list': latest_profile_list}
    return HttpResponse(template.render(context, request))

def pet_detail(request, pet_id):
    pet_profile = get_object_or_404(Profile, pk=pet_id)
    return render(request, 'pets/pet_detail.html', {'pet_profile': pet_profile})