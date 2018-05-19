from flask import Flask, jsonify
# import sys
import os

# the all-important app variable:
app = Flask(__name__)

@app.route('/v1/uploader', methods=['POST'])
def uploader():
    return jsonify({'value':os.getcwd()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80) # Webserver
    # app.run(host='127.0.0.1', debug=True, port=8080) # Localhost (Cloud 9)