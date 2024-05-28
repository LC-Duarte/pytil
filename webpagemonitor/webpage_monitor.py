import logging
import time
from bs4 import BeautifulSoup
import os
import pycurl
import certifi
from io import BytesIO

#from twilio.rest import Client
URL_TO_MONITOR = "https://medium.com/swlh/tutorial-creating-a-webpage-monitor-using-python-and-running-it-on-a-raspberry-pi-df763c142dac" #change this to the URL you want to monitor
DELAY_TIME = 15 # seconds
log = logging.getLogger(__name__)
def process_html(string):
    soup = BeautifulSoup(string, features="lxml")

    # make the html look good
    soup.prettify()

    # remove script tags
    for s in soup.select('script'):
        s.extract()

    # remove meta tags 
    for s in soup.select('meta'):
        s.extract()
    
    # convert to a string, remove '\r', and return
def webpage_was_changed(): 
    """Returns true if the webpage was changed, otherwise false."""
    response = culr_get(URL_TO_MONITOR)
    # create the previous_content.txt if it doesn't exist
    if not os.path.exists("previous_content.txt"):
        open("previous_content.txt", 'w+').close()
    
    filehandle = open("previous_content.txt", 'r')
    previous_response_html = filehandle.read() 
    filehandle.close()

    processed_response_html = process_html(response.text)

    if processed_response_html == previous_response_html:
        return False
    else:
        filehandle = open("previous_content.txt", 'w')
        filehandle.write(processed_response_html)
        filehandle.close()


def culr_get(url):
    log.debug(f"requesting: {url}")
    # Creating a buffer as the cURL is not allocating a buffer for the network response
    buffer = BytesIO()
    c = pycurl.Curl()
    #initializing the request URL
    c.setopt(c.URL, url)
    #setting options for cURL transfer  
    c.setopt(c.WRITEDATA, buffer)
    #setting the file name holding the certificates
    c.setopt(c.CAINFO, certifi.where())
    # perform file transfer
    c.perform()
    #Ending the session and freeing the resources
    c.close()
    #retrieve the content BytesIO
    body = buffer.getvalue()
    #decoding the buffer 
    log.debug("response available")
    return body


def main():
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"), format='%(asctime)s %(message)s')
    log.info("Running Website Monitor")
    while True:
        try:
            if webpage_was_changed():
                log.info("WEBPAGE WAS CHANGED.")
                #send_text_alert(f"URGENT! {URL_TO_MONITOR} WAS CHANGED!")
                #send_email_alert(f"URGENT! {URL_TO_MONITOR} WAS CHANGED!")
            else:
                log.info("Webpage was not changed.")
        except Exception as e:
            log.error("Error checking website.")
            print(e)
            return
        time.sleep(DELAY_TIME)


if __name__ == "__main__":
    main()