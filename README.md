# 🚀 Flask + Docker App

This is a simple Python Flask web application that runs inside a Docker container.

---

## 📂 Project Structure

| File               | Description                            |
|--------------------|----------------------------------------|
| `app.py`           | Main Flask application file            |
| `Dockerfile`       | Instructions to build Docker image     |
| `requirements.txt` | Python libraries used in the app       |

---

## 🔧 How to Run This Project

### ✅ Step 1: Clone the Repository

```bash
git clone https://github.com/Shrutika-tayde/flask-docker-app.git
cd flask-docker-app

✅ Step 2: Build and Run the Docker Container
docker build -t flask-app .
docker run -d -p 5000:5000 flask-app







