# Create your views here.
from xml.dom import minidom
from django.db.models import Min
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from bustranit.forms import SearchForm
import gtfs_realtime_pb2
from models import VehiclePositions,Trips,Routes,StopTimes,Stops
import sys

import urllib

@login_required
def home(request):
    return render_to_response('index.html')

@login_required
def findbus(request):
    context_instance=RequestContext(request)
    form=SearchForm(request.POST)
    return render_to_response('findbus.html',{'form':form},context_instance=RequestContext(request))

def searchbus(request):

    """if 'routeNo' in request.GET:
        message = 'You searched for: %r' % request.GET['agent']
        agent=request.GET['agent']
        routeNo=request.GET['routeNo']
        schedule=[]
        routes=Routes.objects.filter(route_short_name=routeNo)
        stop_times=None
        for route in routes:
            print route.route_id
            trips=Trips.objects.filter(route_id=route.route_id)
            for trip in trips:
                print trip.trip_headsign
                stop_times=StopTimes.objects.filter(trip_id=trip.trip_id)
                for stop_time in stop_times:
                    stops=Stops.objects.get(stop_id=stop_time.stop_id)
                    tup={}
                    tup['stop_name']=stops.stop_name
                    tup['arrival_time']=stop_time.arrival_time
                    tup['departure_time']=stop_time.departure_time
                    schedule.append(tup)

               #     print stop_time.departure_time




        print request.GET['routeNo']
    else:
        message = 'You submitted an empty form.'
    return render_to_response('results.html',{'stop_times':schedule})"""

    if "routeNo" in request.GET:
        tripdetails=[]
        dateTimePicker=request.GET['date']
        print dateTimePicker
        routes=Routes.objects.filter(route_short_name=request.GET['routeNo'])
        for route in routes:
            trips=Trips.objects.filter(route_id=route.route_id)
            for trip in trips:
                result={}
                result['tripName']=trip.trip_headsign
                result['trip_id']=trip.trip_id
                stops=StopTimes.objects.filter(trip_id=trip.trip_id,stop_sequence=1)
                for stop in stops:
                    result['startTime']=stop.arrival_time
                tripdetails.append(result)
    return render_to_response('results.html',{'stop_times':tripdetails})

def schedule(request):
    if "trip_id" in request.GET:
        stoptimes=[]
        trip_id=request.GET['trip_id']
        schedules=StopTimes.objects.filter(trip_id=trip_id)
        for schedule in schedules:
            stoptime={}
            print schedule.stop_id
            stoptime["stop_name"]=schedule.stop_id.stop_name
            stoptime["arrival_time"]=schedule.arrival_time
            stoptime["departure_time"]=schedule.departure_time
            stoptimes.append(stoptime)
        print stoptimes
    return render_to_response('schedule.html',{'stoptimes':stoptimes})

def locate(request):
    trip_id=request.GET['trip_id']
    vp=VehiclePositions.objects.filter(trip_id=trip_id)[0]
    print vp.trip_id.trip_id
    return render_to_response('locate.html',{'vehicleposition':vp})
