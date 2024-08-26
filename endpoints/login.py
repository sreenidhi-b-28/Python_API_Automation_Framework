import json
import requests

with open('../config/endpoints.json', 'r') as f:
    data = json.load(f)

register_url = data["register_url"]


class ApiRegister:

    def __init__(self, base_url: str):
        """
        Initializes the UserAPI with the base URL

        Args:
            base_url (str): the base url for the API
        """
        self.base_url = base_url

    def register(self, username: str, password: str= None):
        """
        Registering in the endpoint

        Args:
            :param username: username in string
            :param password: password in string

        :return: response and status code
        """
        url = self.base_url + register_url
        payload = {"username": username, "password": password}
        response = requests.post(url, json=payload)
        return response.status_code, response.json()
