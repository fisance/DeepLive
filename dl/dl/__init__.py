from flask import Flask

app = Flask(__name__)

# Register views
from dl import routes

if __name__ == '__main__':
    app.run(debug=True)