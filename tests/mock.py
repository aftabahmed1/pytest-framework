import pytest
import requests

# Mock GET request to fetch products from DummyJSON
def test_get_products(mocker):
    # Mocking the requests.get method to simulate the API response
    mock_response = mocker.patch('requests.get')
    
    # Define the mock response JSON, similar to what DummyJSON would return
    mock_response.return_value.status_code = 200
    mock_response.return_value.json.return_value = {
        "products": [
            {"id": 1, "title": "Laptop", "price": 1200.0, "stock": 15},
            {"id": 2, "title": "Smartphone", "price": 800.0, "stock": 30}
        ]
    }
    
    # Call the function that makes the API request
    response = requests.get('https://example.com/products')
    
    # Assertions to check if the mock data was returned
    assert response.status_code == 200
    products = response.json()["products"]
    assert len(products) == 2
    assert products[0]["title"] == "Laptop"
    assert products[1]["title"] == "Smartphone"
