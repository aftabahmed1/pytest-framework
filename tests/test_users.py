import pytest
from utils.api_client import APIClient
from base_test import BaseTest
from utils.schema_validator import SchemaValidator

user_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "firstName": {"type": "string"},
        "lastName": {"type": "string"},
        "age": {"type": "integer"},
        "gender": {"type": "string", "enum": ["male", "female", "other"]},
        "email": {"type": "string", "format": "email"},
        "phone": {"type": "string"},
        "ein": {"type": "string"},
        "height": {"type": "number"},
        "weight": {"type": "number"},
    }
    
}

class TestUsersOAuth2:
    """Tests User API with OAuth 2.0 Authentication"""

    def test_get_user_details(self, oauth2_token):
        """Fetch user details using OAuth 2.0 token"""
        headers = {"Authorization": f"Bearer {oauth2_token}"}
        response = APIClient.get("/users/1", headers=headers)
        assert response.status_code == 200, "Failed to fetch user details"
        assert response.json()["id"] == 1
        print(response.json())
        SchemaValidator.validate_json(response.json(), user_schema)
