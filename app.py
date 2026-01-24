from flask import Flask, render_template, request
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

app = Flask(__name__)

# MongoDB Atlas URI (hard-coded)
MONGO_URI = "mongodb+srv://mydb:mydb@cluster.hnmave1.mongodb.net/db?retryWrites=true&w=majority"

# Connect to MongoDB Atlas
try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    client.server_info()  # Force connection
    db = client.get_database()
    subscribers = db.subscribers
    print("Connected to MongoDB Atlas successfully!")
except ServerSelectionTimeoutError as e:
    print("Error connecting to MongoDB Atlas:", e)
    client = None
    db = None
    subscribers = None  # Important: explicitly set to None

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        if subscribers is None:  # ✅ Compare with None
            message = "Database not available."
        else:
            name = request.form.get("name")
            email = request.form.get("email")
            if subscribers.find_one({"email": email}) is None:  # Prevent duplicates
                subscribers.insert_one({"name": name, "email": email})
                message = "Your subscription has been successfully submitted!"
            else:
                message = "You are already subscribed."
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
