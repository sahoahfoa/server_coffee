from flask import Flask
import os
import threading

app = Flask(__name__)

@app.route("/")
def hello():
    return "Coffee Drank!"

# Shutdown the server AFTER sending the response
@app.after_request
def shutdown(response):
    def shutdown_server():
        os._exit(0)  # Terminates the process cleanly
    threading.Timer(0.1, shutdown_server).start()  # Exit after 1 second
    return response  # Return response first, then exit

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
