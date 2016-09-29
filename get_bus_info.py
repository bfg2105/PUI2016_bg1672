from __future__ import print_function
try:
    from urllib.request import urlopen
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse
    from urllib2 import urlopen
#http://python3porting.com/noconv.html

import json
import sys
import csv

if not len(sys.argv) == 4:
    print("Invalid number of arguments. Run as: python  show_bus_locations.py\
    <API_KEY> <Bus Line>")
    sys.exit()

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json\
?key="+sys.argv[1]+\
"&VehicleMonitoringDetailLevel=calls&LineRef="+sys.argv[2]

response = urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

busdata = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
list_full = []

for i in range(len(busdata)):
    lat = busdata[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    lon = busdata[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    if busdata[i]['MonitoredVehicleJourney']['OnwardCalls'] == {}:
        stopname = 'n/a'
        stopstatus = 'n/a'
        continue
    else:
        stopname = busdata[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
        stopstatus = busdata[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']\
        ['Distances']['PresentableDistance']
    bus_stat = [lat,lon,stopname,stopstatus]
    list_full.append(bus_stat)


busfile = open(sys.argv[3], "w")
writer = csv.writer(busfile)
writer.writerows(list_full)
#above three lines of code were taken from classmate Matt Sloane