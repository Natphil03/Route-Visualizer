import requests
import json
import webbrowser

def mainInputs():
    global apikey
    global origin
    global destination
    apikey = str(input("Enter you API Key : "))
    origin = str(input("Enter a starting location (separate City and State with ',') : "))
    destination = str(input("Enter a ending location (separate City and State with ',') : "))
    directionsRequest()

def directionsRequest():
    url = 'http://www.mapquestapi.com/directions/v2/route?key={0}&from={1}&to={2}'.format(apikey, origin, destination)
    requesturl = str(url)
    getRequest = requests.get(requesturl)
    status(getRequest)

def status(getRequest):
    if getRequest.status_code == 200:
        print('Connection Success!')
        results(getRequest)
    elif getRequest.status_code == 404:
        print('Connection Failed!')

def results(getRequest):
    global CurrentSessionID
    content = getRequest.text
    parsed = json.loads(content)
    CurrentSessionID = parsed["route"]["sessionId"]
    TotalDistance = parsed["route"]["distance"]
    print("The Total Distance from {0} to {1} is".format(origin, destination), TotalDistance, "miles!")
    map()

def map():
    routingRequestURL = 'https://www.mapquestapi.com/staticmap/v5/map?session={0}&routeWidth=2&size=500,300@2x&key={1}'.format(CurrentSessionID, apikey)
    webbrowser.open(routingRequestURL)
    print("Success - Opened Map In Browser!")
mainInputs()

