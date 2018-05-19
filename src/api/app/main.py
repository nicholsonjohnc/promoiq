from flask import Flask, request, jsonify
from werkzeug import secure_filename
import boto3
from OpenSSL import SSL


# the all-important app variable:
app = Flask(__name__)

@app.route('/v1/uploader', methods=['POST'])
def uploader():
    # Retrieve file.
    file = request.files['file']
    file_name = secure_filename(file.filename)
    
    # Upload file.
    s3 = boto3.resource('s3')
    s3.Bucket('uploads.promoiq.website').put_object(Key=file_name, Body=file)

    return jsonify({'file_name':file_name})

if __name__ == '__main__':
    context = SSL.Context(SSL.SSLv23_METHOD)
    context.use_privatekey_file('ssl.key')
    context.use_certificate_file('ssl.cert')
    app.run(host='0.0.0.0', debug=True, port=443, ssl_context=context) # Webserver
    # app.run(host='127.0.0.1', debug=True, port=8080) # Localhost (Cloud 9)