from bs4 import BeautifulSoup
import requests
import json

def get_travel_data(start, dest, key):
    """
    This function retrieves travel time between two locations using Bing Maps API.
    
    Args:
      start (str): Origin address.
      dest (str): Destination address.
      key (str): Bing Maps API key.
    
    Returns:
      resource (dict): 
    """
    
    base_url = "https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix"
    params = {
      "origins": start,
      "destinations": dest,
      "travelMode": "driving",
      #"o": "json",
      "key": key,
      "distanceUnit": "mi",
    }
    
    # Send GET request with user agent header
    headers = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)"}
    response = requests.get(base_url, params=params)#, headers=headers)
    #print (response.content)
    # Check for successful response
    if response.status_code == 200:
      dict_obj = json.loads(response.content.decode().replace("b'", "").replace("'", ""))
      return dict_obj['resourceSets'][0]['resources'][0]
    else:
    raise Exception(f"Error getting travel time: {response.status_code}")

#----------------------------------------------------
#Example
#----------------------------------------------------
start = "35.0376,-106.6109"
dest = "61.1810,-149.9978"
key= "BING MAP KEY"
get_travel_data(start, dest, key)

