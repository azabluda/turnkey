import os
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder="../frontend/build", static_url_path="/")

# Enable CORS only if CORS_ORIGINS is set
if os.environ.get("CORS_ORIGINS"):
    CORS(app, origins=os.environ["CORS_ORIGINS"].split(","))

@app.route("/api/message")
def message():
    return jsonify({"message": "Hello from Flask!"})

# Catch-all: serve React app for any non-API route
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react(path):
    if path.startswith('api/'):
        return jsonify({"error": "Not found"}), 404
    if os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
