import urllib.request
import json

# name = input("Enter username: ")
name = 'vessi'
key = ""
data = urllib.request.urlopen(
    "https://www.googleapis.com/youtube/v3/channels?&forUsername="+name+"&key="+key).read()
# subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]

print(name + " has " + str(json.loads(data)))
# print(name + " has " + "{:,d}".format(int(subs)) + " subscribers!🎉")
