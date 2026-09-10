import os
from flask import Flask, jsonify, request

app = Flask(__name__)

# Read application version dynamically from VERSION file if available
def get_version():
    version_file = os.path.join(os.path.dirname(__file__), "VERSION")
    if os.path.exists(version_file):
        with open(version_file, "r") as f:
            return f.read().strip()
    return "1.0.0"

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "application": "student-ml-api",
        "version": "1.1.0"
    }), 200

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True)
    
    # Check for missing payload or missing 'value' key
    if not data or "value" not in data:
        return jsonify({"error": "Missing 'value' in request body"}), 400
    
    val = data["value"]
    
    # Validate numeric input
    if not isinstance(val, (int, float)) or isinstance(val, bool):
        return jsonify({"error": "'value' must be a numeric type"}), 400
    
    # Prediction logic: double the input value
    prediction = val * 2
    return jsonify({
        "input": val,
        "prediction": prediction
    }), 200

if __name__ == "__main__":
    # Bound to 0.0.0.0 so external requests reach inside the container
    app.run(host="0.0.0.0", port=5000)