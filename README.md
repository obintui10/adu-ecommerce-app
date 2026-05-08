## 🛒 ADU E‑Commerce App
A simple Flask + MongoDB Atlas application that allows users to subscribe with their name and email. Built with containerization in mind using Docker, and structured for scalability and recruiter visibility.

![Python](https://img.shields.io/badge/python-3.11-blue)
![Flask](https://img.shields.io/badge/flask-3.0.0-lightgrey)
![MongoDB Atlas](https://img.shields.io/badge/mongoDB-Atlas-green)
![Docker](https://img.shields.io/badge/docker-ready-blue)

## 🚀 Quickstart
```bash
# Clone the repo
git clone https://github.com/yourusername/adu-ecommerce-app.git
cd adu-ecommerce-app

# Build Docker image
docker build -t adu-ecommerce-app .

# Run container
docker run -p 80:80 adu-ecommerce-app

## 🗂️ Project Structure
```bash
adu-ecommerce-app/
│── app.py              # Flask app entry point
│── requirements.txt    # Dependencies
│── Dockerfile          # Container setup
│── templates/
│   └── index.html      # Subscription form template
│── static/
│   └── style.css       # Styling

 ## 📐 Architecture Diagram

 +-------------------+
|     Browser       |
|  (User submits    |
|   subscription)   |
+---------+---------+
          |
          v
+-------------------+
|   Flask App       |
|   (app.py)        |
|-------------------|
| - Renders index   |
| - Handles POST    |
| - Validates email |
+---------+---------+
          |
          v
+-------------------+
|  MongoDB Atlas    |
|  (subscribers     |
|   collection)     |
|-------------------|
| - Stores name     |
| - Stores email    |
| - Prevents dupes  |
+-------------------+

```
## 🗂 Mermaid Diagram
```mermaid
flowchart TD
    A[Browser (User submits subscription)] --> B[Flask App (app.py)]
    B --> C[MongoDB Atlas (subscribers collection)]

    classDef flask fill:#f9f,stroke:#333,stroke-width:1px;
    classDef db fill:#9f9,stroke:#333,stroke-width:1px;

    class B flask
    class C db


