import json
import requests

class Requester:
    def __init__(self):
        self.url = "http://127.0.0.1:5000"
        
    def request(self, method, endpoint, params=None):
        url = self.url + endpoint
        
        
        if method == "GET":
            r = requests.get(url, parmas=params)
            return r.text
        else:
            r = requests.post(url, data=params)
            return r.json()

    def login(self, username, real_name):
        endpoint = "/user_exists"
        params = {"username": username}

        user_exists = self.request("POST", endpoint, params)

        return user_exists["exists"]

    def create_account(self, username, real_name):
        endpoint = "/user_exists"
        params = {"username": username}
        exists = self.request("POST", endpoint, params)

        if exists["exists"]:
            return False
        
        endpoint = "/add_user"
        params["real_name"] = real_name

        self.request("POST", endpoint, params)
        return True

    def get_all_users(self):
        endpoint = "/get_all_users"
        users = self.request("GET", endpoint)

        return json.loads(users)

    