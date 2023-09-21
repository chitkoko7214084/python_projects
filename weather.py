import json
#import json files
import ssl
#https certificate
from urllib.request import urlopen


def CAAlert():
    url="https://api.weather.gov/alerts/active?area=CA"
    #after line 8 the code with generate json file
    context=ssl._create_unverified_context()
    #if something wrong with communication 
    response= urlopen(url, context=context)
    weatherData = json.loads(response.read())
    #weatherdata contains all the information 
    return weatherData["features"][0]["properties"]["event"]


def main():
    state = input("Enter two charatcter state code:")
    url="https://api.weather.gov/alerts/active?area=" +state
    #after line 8 the code with generate json file
    context=ssl._create_unverified_context()
    #if something wrong with communication 
    response= urlopen(url, context=context)
    weatherData = json.loads(response.read())
    for e in weatherData("features"):
        print(e["properties"]["event"])
        print(e["properties"]["headlines"])
        print(e["properties"]["description"])
        
    
    
    main()
    
    
