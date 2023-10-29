import requests

class Nutritionix():
    def __init__(self):
        self.base_url = r"https://trackapi.nutritionix.com/v2/search/item?upc="
        self.payload = {}
        self.headers = {
        'x-app-id': 'af49e411',
        'x-app-key': 'c500c3a3eafd8a14b48de7a1f01293c9'
        }
        self.request_status_good = True

    def make_request(self,upc):
        url = self.base_url+str(upc)
        self.response = requests.request("GET", url=url, headers=self.headers, data=self.payload)
        if self.response.status_code == 404:
            print(f"response status code : {self.response.status_code}")
            return None

        else:
            print(f"{self.response.json()}")
            return self.response.json()
