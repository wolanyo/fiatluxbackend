#from urllib2 import *
import json
import urllib.request

API_KEY="AIzaSyB26iRVOgAhMkgktoDTYrOSoJb_RCzdttM"
GCM_SERVER = "https://gcm-http.googleapis.com/gcm/send"
HEADER = {"Authorization": "key=" + API_KEY, "Content-type": "application/json"}

TO_POST= "/topics/article"
TO_STORY = "/topics/story"
TO_SHOP = "/topics/shop"
TO_MEDIA_ARCHIVE = "/topics/mediaarchive"
TO_LESSON = "/topics/lesson"


def sendNotification(message):

    data = {
        "to": "/topics/article",
        "notification": {
            "body": message,
            "title": "FiatLux",
            "icon": "fiatlux_48"
        }
    }

    dataAsJSON = json.dumps(data).encode('utf8')
    request = urllib.request.Request(GCM_SERVER, data=dataAsJSON, headers=HEADER)
    urllib.request.urlopen(request)