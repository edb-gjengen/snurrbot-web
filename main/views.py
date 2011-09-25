from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, InvalidPage

from main.models import *

def home(request):
    entry_list = Entry.objects.all().order_by('created').reverse()
    paginator = Paginator(entry_list, 10) # Show 25 entries per page

    # Make sure page request is an int. If not, deliver first page
    try:
        page = int(request.GET.get('page','1'))
    except ValueError:
        page = 1

    # If page is out of range (e.g. 9999), deliver last page of results.
    try:
        entries = paginator.page(page)
    except (EmptyPage, InvalidPage):
        entries = paginator.page(paginator.num_pages)

    print entries.__dict__

    return render_to_response('home.html', locals(), context_instance=RequestContext(request))
