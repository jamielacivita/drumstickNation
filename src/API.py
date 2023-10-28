import requests

class Nutritionix():
    def __init__(self,upc):
        self.url = r"https://trackapi.nutritionix.com/v2/search/item?upc="+str(upc)
        self.payload = {}
        self.headers = {
        'x-app-id': 'af49e411',
        'x-app-key': 'c500c3a3eafd8a14b48de7a1f01293c9'
        }

    def make_request(self):
        self.response = requests.request("GET", self.url, headers=self.headers, data=self.payload)

        #return self.response.text
        return self.response.json()



