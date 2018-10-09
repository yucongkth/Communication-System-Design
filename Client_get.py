#created by yucong

import requests

class Do_get():
    def __init__(self,url):
        self.url=url

    def get_data(self):

        data = requests.get(self.url)
        nfm_data = data.json()
        return nfm_data


