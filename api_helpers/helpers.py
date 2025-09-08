import os

import requests
from faker import Faker
from requests.auth import HTTPBasicAuth


class APIHelpers:

    def __init__(self,generate_token,base_url,user_name,password):
        self.generate_token = generate_token
        self.base_url = base_url
        self.user_name = user_name
        self.password = password

    def create_user(self):
        fake = Faker()
        url = f"{self.base_url}/Account/v1/User"
        payload = {
            "userName": fake.name(),
            "password": "Mackenzie@02021992"
        }
        print(payload["userName"])
        response = requests.post(url=url,json=payload,headers=self.generate_token)
        return response

    def delete_user_without_auth_header(self,create_user_response):
        user_json = create_user_response.json()
        uuid = user_json["userID"]
        url = f"{self.base_url}/Account/v1/User/{uuid}"
        response = requests.delete(url)
        return response

    def delete_user(self,create_user_response):
        user_json = create_user_response.json()
        uuid = user_json["userID"]
        url = f"{self.base_url}/Account/v1/User/{uuid}"
        print(self.user_name,self.password)
        response = requests.delete(url,auth=HTTPBasicAuth(self.user_name,self.password))
        return response

    def testing_addoption_hook(self,request):
        addoption_value = request.config.getoption("--testrun")
        print(addoption_value)



