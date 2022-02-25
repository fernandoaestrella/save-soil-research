# users require ids, channels require forUsername
import urllib.request
import json

# name = input("Enter username: ")
# name = 'UCZAG5hXyBiV-jRosndVfRDQ'
name = 'Reuters'
key = 'AIzaSyDOvAD0fHHxszJDScdqKuCjJrVpTLntfJM'
# data = urllib.request.urlopen(
#     "https://www.googleapis.com/youtube/v3/search?part=snippet&type=channel&maxResults=1&q="+name).read()
# print(name + " has " + str(json.loads(data)))

data = urllib.request.urlopen(
    "https://www.googleapis.com/youtube/v3/channels?part=statistics,snippet&type=channel&id="+name+"&key="+key).read()
# subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]

print(name + " has " + str(json.loads(data)))
# print(name + " has " + "{:,d}".format(int(subs)) + " subscribers!🎉")
