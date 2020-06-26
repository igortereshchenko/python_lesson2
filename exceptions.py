# try:
#     print(1)
#     print(1/0)
#
#
# except ZeroDivisionError:
#     print("divizion error")
#
# except Exception:
#     print("general")
#
# except ValueError:
#     print("error")


import requests
try:
    response = requests.get('https://httpbin.org/status/500')

    print(response.headers)
    # TODO
    response.raise_for_status()

except requests.exceptions.ConnectTimeout:
    print('timeout error')
except requests.exceptions.ConnectionError:
    print("ulr doesnt exists")
except requests.exceptions.HTTPError as err:
    # TODO
    print(err.response.headers, 'some error')





