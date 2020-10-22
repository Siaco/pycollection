import urllib.request
import json
import argparse

parser = argparse.ArgumentParser(description='Print the last alert issued for Frosinone by Protezione Civile Italiana')
args = parser.parse_args()

url = "http://webservices.ingv.it/fdsnws/event/1/query?starttime=1975-01-01T00%3A00%3A00&endtime=2020-10-22T23%3A59%3A59&minmag=0&maxmag=10&mindepth=-1000&maxdepth=1000&minlat=-90&maxlat=90&minlon=-180&maxlon=180&minversion=100&orderby=time-asc&format=text&limit=15000"

req = urllib.request.Request(url)

r = urllib.request.urlopen(req).read()

header = ['#EventID', 'Time', 'Latitude', 'Longitude', 'Depth/Km', 'Author', 'Catalog', 'Contributor', 'ContributorID',
          'MagType', 'Magnitude', 'MagAuthor', 'EventLocationName']

data = {}

dataS = r.decode('utf-8')

dataS = dataS.split('\n')

for terremoto in dataS:
    campi = terremoto.split('|')
    i = 0
    jsonElement = {}
    for campo in campi:
        jsonElement[header[i]] = campo
        i += 1
    data[jsonElement['#EventID']] = jsonElement

with open('terremoti.json', 'w') as outfile:
    json.dump(data, outfile)
