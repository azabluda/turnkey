import json
from flask import Flask, request, jsonify
from app import lambda_handler

app = Flask(__name__)

@app.route("/", defaults={"path": ""}, methods=["GET", "POST", "PUT", "DELETE"])
@app.route("/<path:path>", methods=["GET", "POST", "PUT", "DELETE"])
def catch_all(path):
    """
    A catch-all route that simulates API Gateway.
    """
    # Create a mock event object
    event = {
        "httpMethod": request.method,
        "path": f"/{path}",
        "queryStringParameters": dict(request.args),
        "headers": dict(request.headers),
        "body": request.get_data().decode("utf-8")
    }

    # Call the lambda handler
    result = lambda_handler(event, None)

    # Return the response
    return (
        result["body"],
        result["statusCode"],
        result["headers"]
    )

if __name__ == "__main__":
    app.run(debug=True, port=5001)