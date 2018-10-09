#created by yucong


import requests
import json

class Do_post():
    def __init__(self,url,nfm_data):
        self.url=url
        self.data=nfm_data
        print(type(self.data))
    def post(self):
        headers = {'Content-Type': 'application/json'}
        data = json.dumps(self.data)

        response = requests.post(url=self.url, headers = headers, data = data)
        print(response.text)


