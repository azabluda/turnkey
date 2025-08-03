import json
import unittest
from ..app import lambda_handler

class TestApp(unittest.TestCase):
    def test_lambda_handler(self):
        """
        Test that the lambda_handler returns a 200 status code and the correct message.
        """
        # Create a mock event
        event = {
            "httpMethod": "GET",
            "path": "/",
            "queryStringParameters": {},
            "headers": {},
            "body": ""
        }

        # Call the lambda handler
        result = lambda_handler(event, None)

        # Check the result
        self.assertEqual(result["statusCode"], 200)
        self.assertEqual(result["headers"]["Content-Type"], "application/json")
        self.assertEqual(json.loads(result["body"]), {"message": "Hello from Lambda!"})

if __name__ == "__main__":
    unittest.main()