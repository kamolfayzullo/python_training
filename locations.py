import requests


def getLatLon():
    response = requests.get("https://ipinfo.io/json")
    geodata=response.json()['loc']
    lat=float(geodata.split(',')[0])
    lon=float(geodata.split(',')[1])
    return lat,lon

lat,lon=getLatLon()
print('lat:',lat)
print('lon:',lon)