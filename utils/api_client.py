import requests
from utils.config import BASE_URL, HEADERS

class APIClient:
    """Reusable API client for making requests."""

    @staticmethod
    def get(endpoint,headers=None, params=None):
        """Reusable GET request"""
        response = requests.get(f"{BASE_URL}{endpoint}", headers=HEADERS, params=params)
        return response

    @staticmethod
    def post(endpoint, json):
        """Reusable POST request"""
        response = requests.post(f"{BASE_URL}{endpoint}", json=json, headers=HEADERS)
        return response

    @staticmethod
    def put(endpoint, payload):
        """Reusable PUT request"""
        response = requests.put(f"{BASE_URL}{endpoint}", json=payload, headers=HEADERS)
        return response

    @staticmethod
    def delete(endpoint):
        """Reusable DELETE request"""
        response = requests.delete(f"{BASE_URL}{endpoint}", headers=HEADERS)
        return response
