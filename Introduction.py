from flask import Flask

# Create a Flask application instance
# __name__ helps Flask determine the root path of the application
app = Flask(__name__)

# Define a route for the root URL ('/')
# This decorator maps the URL to the home function
@app.route('/')
def home():
    # Return HTML content that will be displayed in the browser
    return "<h1>YOOOOOOOOO</h1>"