from flask import Flask

app = Flask(__name__)

#Let's create endpoints
@app.route('/')
def home():
    return "<h1>Flask WebAPI</h1>"

@app.route('/ping')
def pinger():
    return {"messege": "Hello, there!"}
