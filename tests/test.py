import unittest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestECommerceAPI(unittest.TestCase):
    # Test for GET / endpoint
    def test_get_root(self):
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Welcome to the E-commerce website."})

    # Test for GET /health-check endpoint
    def test_health_check(self):
        response = client.get("/health-check")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Ok")

    # Add more test cases for other endpoints such as users, products, and orders

    # Test for GET /users endpoint
    def test_get_users(self):
        response = client.get("/users")
        self.assertEqual(response.status_code, 200)
        # Add more assertions to validate response data

    # # Test for GET /users/{id} endpoint
    # def test_get_user_by_id(self):
    #     response = client.get("/users/1")  # Assuming user with ID 1 exists
    #     self.assertEqual(response.status_code, 200)
    #     # Add more assertions to validate response data

    # # Test for POST /users endpoint
    # def test_create_user(self):
    #     new_user = {
    #         "name": "Test User",
    #         "email": "test@example.com",
    #         "address": "Test Address",
    #         "mobile": 1234567890
    #     }
    #     response = client.post("/users", json=new_user)
    #     self.assertEqual(response.status_code, 201)
    #     # Add more assertions to validate response data

    # # Test for DELETE /users/{id} endpoint
    # def test_delete_user(self):
    #     response = client.delete("/users/1")  # Assuming user with ID 1 exists
    #     self.assertEqual(response.status_code, 200)
    #     # Add more assertions to validate response data

    # # Test for PUT /users/{id} endpoint
    # def test_update_user(self):
    #     updated_user = {
    #         "name": "Updated Test User",
    #         "email": "updated_test@example.com",
    #         "address": "Updated Test Address",
    #         "mobile": 9876543210
    #     }
    #     response = client.put("/users/1", json=updated_user)  # Assuming user with ID 1 exists
    #     self.assertEqual(response.status_code, 200)
    #     # Add more assertions to validate response data

if __name__ == '__main__':
    unittest.main()