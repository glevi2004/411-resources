from mimetypes import init
from types import MethodDescriptorType
from urllib import response
from flask import Flask, make_response, request, jsonify
import os
import time


app = Flask(__name__)

@app.route('/')
def hello():
    response = make_response(
        {
            'response': 'Hello, World!',
            'status': 200
        }
    )
    return response

# New '/repeat' route to handle GET parameter "input
@app.route('/repeat', methods=['GET'])
def repeat():
    user_input = request.args.get('input', 'No input provided')
    reponse = {
        "body": user_input,
        "status": 200
    }
    return jsonify(reponse)

# Expose one function at both '/health' and '/healthcheck'
@app.route('/health')
@app.route('/healthcheck')
def health():
    return jsonify({"body": "OK", "status": 200}) #shared function for both endpoints

# New '/hang' endpoint that causes the server to freeze
@app.route('/hang')
def hang():
    while True: # Infinite loop (intentionally crashing Flask)
        time.sleep(1)


if __name__ == '__main__':
    # By default flask is only accessible from localhost.
    # Set this to '0.0.0.0' to make it accessible from any IP address
    # on your network (not recommended for production use)
    port = int(os.getenv("PORT", 5002)) # Default o 5002 if port not setyp since I am using mac
    app.run(host='0.0.0.0', port=port, debug=True, threaded=False) # Run Flask in single-threaded mode
    # flask normally handles mutiple requests in seperate threads
    # this ensures when /hand is called entire server will freeze

