from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from main.models import *

def home(request):

    entries = Entry.objects.all().order_by('created').reverse()

    return render_to_response('home.html', locals(), context_instance=RequestContext(request))
