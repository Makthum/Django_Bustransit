# Create your views here.
from xml.dom import minidom
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
import urllib

@login_required
def home(request):
    return render_to_response('index.html')

@login_required
def findbus(request):
    context_instance=RequestContext(request)
    return render_to_response('findbus.html',context_instance)

def searchbus(request):
    if 'routeNo' in request.GET:
        message = 'You searched for: %r' % request.GET['agent']
        agent=request.GET['agent']
        f = urllib.urlopen('http://webservices.nextbus.com/service/publicXMLFeed?command=schedule&a=ttc&r=68&direction=North')
        myfile = f.read()
        xmldoc = minidom.parseString(myfile)
        itemlist = xmldoc.getElementsByTagName('route')
        print len(itemlist)
        print itemlist[0].attributes['title'].value
        for s in itemlist :
            print s.attributes['title'].value
        print agent
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(myfile)