import pytest
from utils.api_client import APIClient
from dotenv import load_dotenv
import os

load_dotenv()

# ✅ Correct way to pass parameters directly inside the fixture
@pytest.fixture(scope="function", params=[
    ("Laptop", 1500, 10),
    ("Smartphone", 800, 5),
    ("Headphones", 100, 20),
])
def new_product(request):
    """Fixture to create a new product before test and delete after test."""
    title, price, stock = request.param  # ✅ Correctly accessing param values

    payload = {
        "title": title,
        "price": price,
        "stock": stock
    }
    
    response = APIClient.post("/products/add", json=payload)
    assert response.status_code == 201, f"❌ Product creation failed: {response.json()}"
    product = response.json()

    # Validate response
    assert product["title"] == title
    assert product["price"] == price
    assert product["stock"] == stock

    yield product  # Provide test data to the test case

    # Cleanup: Delete product after test
    delete_response = APIClient.delete(f"/products/1")
    assert delete_response.status_code == 200, f"❌ Product deletion failed: {delete_response.json()}"

def test_create_product(new_product):
    """Test creating multiple products using parameterized fixture."""
    product = new_product  # Fixture provides the product

    print(f"✅ Created Product: {product['id']} - {product['title']}")

    # Validate response
    assert "id" in product, "❌ Product ID is missing!"
    assert product["title"], "❌ Product title is missing!"


@pytest.fixture(scope="session")
def oauth2_token():
    """Fixture to fetch an OAuth 2.0 Bearer Token"""
    response = APIClient.post("/auth/login", json={
        "username": os.getenv("OAUTH_2_USERNAME"),
        "password": os.getenv("OAUTH_2_PASSWORD")
    })
    assert response.status_code == 200, "OAuth 2.0 Authentication Failed!"
    return response.json().get("accessToken")
