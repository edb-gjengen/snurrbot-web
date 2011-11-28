import simplejson as json
from datetime import datetime

from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, InvalidPage

from models import *

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

    return render_to_response('home.html', locals(), context_instance=RequestContext(request))

def log(request):
    entry_list = Entry.objects.raw("SELECT id, user, COUNT( * ) as entries, DATE( created ) AS date FROM `main_entry` GROUP BY user, DATE( created )")
    if isinstance(entry_list[0].date, unicode):
        entry_list = [ (e.user,e.date,e.entries) for e in entry_list]
    else:
        # In Django trunk dates in raw queries are recognized and converted to datetime objects
        entry_list = [ (e.user,e.date.strftime("%Y-%m-%d"),e.entries) for e in entry_list]
    #LORD!
    per_user = {}
    for user, date, es in entry_list:
        data = (date, es)

        if user in per_user:
            # sum up data
            data = (data[0], per_user[user][-1:][0][1] + data[1])
            per_user[user].append(data)
        else:
            per_user[user] = []
            per_user[user].append(data)

    return HttpResponse(json.dumps(per_user), content_type='application/javascript; charset=utf8')
