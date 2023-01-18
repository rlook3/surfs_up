from flask import flask

# Create a Flask App instance
app = Flask(__name__)

# Create a Flask Route
@app.route('/')
def hello_world():
    return 'Hello world'
