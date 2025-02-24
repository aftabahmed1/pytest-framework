import pytest
from utils.api_client import APIClient
from base_test import BaseTest

class TestProducts(BaseTest):
    
    def test_get_all_products(self):
        """Test fetching all products"""
        response = APIClient.get("/products")
        assert response.status_code == 200
        assert "products" in response.json()
    
    def test_create_product(self, new_product):
        """Test creating a new product"""
        assert new_product["title"] is not None
    
    def test_update_product(self, new_product):
        """Test updating a product"""
        product_id = 1
        payload = {"price": 20.99}
        response = APIClient.put(f"/products/{product_id}", payload)
        assert response.status_code == 200
        assert response.json()["price"] == 20.99
    
    def test_delete_product(self, new_product):
        """Test deleting a product"""
        product_id = 1
        response = APIClient.delete(f"/products/{product_id}")
        assert response.status_code == 200
