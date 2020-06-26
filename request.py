import urllib.request
import requests

response = urllib.request.urlopen("https://google.com")

print(response.getcode())

parameters = ['java','python', 'c#']

for parameter in parameters:
    response = requests.get("https://www.google.com/search?q={0}".format(parameter))

    print(response.headers['server'])
    print(response.content)



# Auth

auth_request = urllib.request.HTTPPasswordMgrWithDefaultRealm()
auth_request.add_password(None,'https://httpbin.org//basic-auth/user/passwd','user','passwd')

handler = urllib.request.HTTPBasicAuthHandler(auth_request)

open_handler = urllib.request.build_opener(handler)

response = open_handler.open('https://httpbin.org//basic-auth/user/passwd')

print(response.read())



