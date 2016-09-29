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

if not len(sys.argv) == 3:
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

bus = sys.argv[2]
print ('Bus Line : ', bus)
print ('Number of Active Buses : ', len(busdata))
for i in range(len(busdata)):
    print ('Bus ', i, 'is at latitude', busdata[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'], 'and longitude ', busdata[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
