from flask import Flask
import sys

# the all-important app variable:
app = Flask(__name__)

@app.route("/")
def hello():
    return "Oh, Hello World"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80) # Webserver
    # app.run(host='127.0.0.1', debug=True, port=8080) # Localhost (Cloud9)