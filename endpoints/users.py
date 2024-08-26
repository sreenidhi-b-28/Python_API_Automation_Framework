import json
import requests

with open('../config/endpoints.json', 'r') as f:
    data = json.load(f)

list_users_url = data["list_users_url"]
list_resource_details_url = data["list_resource_details_url"]
users_url = data["users_url"]


class ApiUsers:

    def __init__(self, base_url: str):
        """
        Initializes the UserAPI with the base URL

        Args:
            base_url (str): the base url for the API
        """
        self.base_url = base_url

    def list_users(self):
        """
        Get the list of users

        Returns:
            response: returns the status code and the response of the get requests URL
        """
        url = self.base_url + list_users_url
        response = requests.get(url)
        return response.status_code, response.json()

    def list_resource_details(self):
        """
        Get the list of resource details for the users

        Returns:
            response: the response of the get requests URL
        """
        url = self.base_url + list_resource_details_url
        response = requests.get(url)
        return response.status_code, response.json()

    def create_users(self, name: str, job: str):
        """
        Create the users

        Returns:
            response: the response of the get requests URL
        """
        url = self.base_url + users_url
        payload = {"name": name, "job": job}
        response = requests.post(url, json=payload)
        return response.status_code, response.json()

    def update_user(self, name: str, job: str):
        """
        Create the users

        Returns:
            response: the response of the get requests URL
        """
        url = self.base_url + users_url + "/2"
        payload = {"name": name, "job": job}
        response = requests.post(url, json=payload)
        return response.status_code, response.json()

    def partial_update_user(self, job: str):
        """
        Create the users

        Returns:
            response: the response of the get requests URL
        """
        url = self.base_url + users_url + "/2"
        payload = {"job": job}
        response = requests.post(url, json=payload)
        return response.status_code, response.json()
