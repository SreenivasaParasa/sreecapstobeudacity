
from flask import Flask
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@app.route('/')
def hello_world():
    logger.info('Hello, world!')
    return 'Hello, world!'

if __name__ == '__main__':
    # Run the Flask app 
    app.run(host='0.0.0.0', port=80, debug=True)
