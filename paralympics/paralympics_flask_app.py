# Import the Flask and escape
from flask import Flask
from markupsafe import escape

paralympics_app = Flask(__name__)

@paralympics_app.route('/<name>')
def hello_world(name):
    return f'Hello {escape(name)} and Welcome to the Paralympics App'

# Run the app
if __name__ == '__main__':
    paralympics_app.run(debug=True)

# Run by using the link & changing http://127.0.0.1:5000/name eg http://127.0.0.1:5000/Shane