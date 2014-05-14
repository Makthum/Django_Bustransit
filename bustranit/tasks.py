from __future__ import absolute_import
import urllib
from celery import Celery, task, current_task, shared_task

from bustranit import gtfs_realtime_pb2
from bustranit.models import Trips, Routes, VehiclePositions

__author__ = 'zarroc'


@task(name='loadrealtimedata')
def load_realtime():
    urllib.urlretrieve("http://rtu.york.ca/gtfsrealtime/VehiclePositions","VehiclasdasePositions")
    print "File Downloaded"
    f = open("/home/zarroc/Downloads/VehiclePositions", "rb")
    data=gtfs_realtime_pb2.FeedMessage()
    data.ParseFromString(f.read())
    for entity in data.entity:
        ventity=entity.vehicle
        trip=Trips.objects.get(trip_id=ventity.trip.trip_id)
        if ventity.trip.route_id !="":
            route=Routes.objects.get(route_id=ventity.trip.route_id)
        vp=VehiclePositions(route_id=None,trip_id=trip)
        vp.save()
