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

✅ Step 2: Build the Docker Image
docker build -t flask-docker-app .

✅ Step 3: Run the Docker Container
docker run -d -p 5000:5000 flask-docker-app

🌐 Access the App
Visit: http://localhost:5000

Or if on AWS EC2: http://<your-ec2-public-ip>:5000

You should see: Hello from Flask inside Docker!






