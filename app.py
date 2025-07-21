from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Hello from Flask running in Docker on EC2 Ubuntu!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

