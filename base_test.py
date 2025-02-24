import pytest
import requests
from utils.config import BASE_URL, HEADERS

class BaseTest:
    """Base Test class for API tests to handle common setup & teardown."""

    def setup_method(self):
        """Setup method runs before each test"""
        print("\n🔄 Setting up test environment...")

    def teardown_method(self):
        """Teardown method runs after each test"""
        print("\n✅ Cleaning up after test execution...")
