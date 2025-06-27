from flask import Flask

# Step 1: Create a Flask app instance
app = Flask(__name__)

# Step 2: Define a route (homepage)
@app.route("/")
def home():
    return "<h1>Welcome to My Flask App!</h1><p>This is running on localhost.</p>"

# Step 3: Run the app (only when run directly)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
