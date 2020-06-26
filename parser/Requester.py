import os
import time
from random import randint

from selenium import webdriver
from urllib3 import ProxyManager, make_headers, PoolManager, disable_warnings

class Requester:
    """
    Class to perform https/http request
    """

    def __init__(self, url, retries=4, timeout=30, sleep_time=10):
        self.__url = url
        self.__retries = retries
        self.__timeout = timeout
        self.__sleep_time = sleep_time


        dir_path = os.path.dirname(os.path.realpath(__file__))
        chromedriver = os.path.join(dir_path, 'drivers', 'chromedriver.exe')

        options = webdriver.ChromeOptions()

        options.add_argument('headless')
        options.add_argument('window-size=1200x600')  # optional

        self.__browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)

        self.__http = PoolManager()

    def __del__(self):
        self.__browser.close()

    def make_get_request(self, parameters=None):
        status = None
        html_content = None

        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}


        try:
            for tries in range(self.__retries):
                try:

                    # http request
                    response = self.__http.request('GET', self.__url, headers=headers, fields=parameters,
                                                   timeout=self.__timeout)

                    status = response.status
                    html_content = response.data
                #     TODO
                # if content ok break
                #    1 way
                    self.__browser.get("data:text/html;charset=utf-8,{html_content}".format(html_content=html_content))
                    html_content = self.__browser.page_source

                    return html_content

                #    2 way
                # self.__browser.get(self.__url, headers=headers, fields=parameters,
                #                                                    timeout=self.__timeout)



                except TimeoutError:
                    html_content=None
                    random_delta = randint(1, self.__sleep_time)
                    time.sleep(self.__sleep_time * tries + random_delta)
                    pass

        except ConnectionError:
            print('bad ping')
            html_content=None

        return html_content


if __name__=="__main__":

    requester = Requester("https://google.com/search")

    for i in range(100):
        print(requester.make_get_request({'q':'java'}))