from flask import Flask, request
import logging
from datetime import datetime

app = Flask(__name__)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    handlers=[
        logging.FileHandler("server.log"),
        logging.StreamHandler()
    ]
)


    

@app.route('/')
def hello_world():
    user_agent = request.headers.get('User-Agent', 'Unknown')
    ip_address = request.remote_addr
    timezone = request.headers.get('Time-Zone', 'Unknown')
    header = request.headers
    
    logging.info(f"IP Address: {ip_address}")
    logging.info(f"User Agent: {user_agent}")
    logging.info(f"Time-Zone: {timezone}")
    logging.info(f"{header}")
    
    return "Hello World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
