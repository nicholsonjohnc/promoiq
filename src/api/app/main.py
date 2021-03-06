from flask import Flask, request, jsonify
from werkzeug import secure_filename
import boto3
from flask_cors import CORS

# the all-important app variable:
app = Flask(__name__)
CORS(app)

@app.route('/v1/uploader', methods=['POST'])
def uploader():
    # Retrieve file.
    file = request.files['file']
    file_name = secure_filename(file.filename)
    
    # Upload file.
    s3 = boto3.resource('s3')
    s3.Bucket('uploads.promoiq.website').put_object(Key=file_name, Body=file)

    return jsonify({'file_name':file_name})
    
@app.route('/v1/test', methods=['GET'])
def test():
    return jsonify({'test':1})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80) # Webserver
    # app.run(host='127.0.0.1', debug=True, port=8080) # Localhost (Cloud 9)