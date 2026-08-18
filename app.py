from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "ECS Version 2 Deployment"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)