import unittest
from fastapi.testclient import TestClient

from main import app


class TestApp(unittest.TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)

    def test_root_endpoint(self) -> None:
        response = self.client.get("/")
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json(), {"message": 'Service "a" is healthy.'})


if __name__ == "__main__":
    unittest.main()
