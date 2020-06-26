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

str =  'pythön!'

# encoding

response = requests.get("https://api.github.com/")
print(response.encoding)

# encoding convertrer
text = 'some str'
print(text.encode())

from sys import getdefaultencoding

print(getdefaultencoding())
test = 'ЪЪЇііІ & hello'
print(test.encode())
print(test.encode('ascii', errors='ignore'))
print(test.encode('ascii', errors='replace'))
print(test.encode('ascii', errors='xmlcharrefreplace'))
print(test.encode('ascii', errors='backslashreplace'))

text_encoded = '\xd0\xaa\xd0\xaa\xd0\x87\xd1\x96\xd1\x96\xd0\x86'.encode()

print(text_encoded.decode(encoding='UTF-8', errors='strict'))