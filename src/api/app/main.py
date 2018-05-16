from flask import Flask, jsonify
import sys

# the all-important app variable:
app = Flask(__name__)

@app.route('/v1/analyze', methods=['POST'])
def hello():
    return jsonify({'value':5})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80) # Webserver
    # app.run(host='127.0.0.1', debug=True, port=8080) # Localhost (Cloud 9)