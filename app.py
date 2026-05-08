import os
from flask import Flask, render_template, request
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

app = Flask(__name__)

# Load MongoDB URI from environment variable
MONGO_URI = os.environ.get("MONGO_URI")

try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    client.server_info()
    db = client.get_database()
    subscribers = db.subscribers
    print("Connected to MongoDB Atlas successfully!")
except ServerSelectionTimeoutError as e:
    print("Error connecting to MongoDB Atlas:", e)
    client = None
    db = None
    subscribers = None

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        if subscribers is None:
            message = "Database not available."
        else:
            name = request.form.get("name")
            email = request.form.get("email")
            if email and "@" in email:  # simple validation
                if subscribers.find_one({"email": email}) is None:
                    subscribers.insert_one({"name": name, "email": email})
                    message = "Your subscription has been successfully submitted!"
                else:
                    message = "You are already subscribed."
            else:
                message = "Invalid email format."
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
