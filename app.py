from flask import Flask
import sys

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Server will exit after this request', 200

@app.after_request
def after_request(response):
    sys.exit()  # Exits the server after handling one request
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
