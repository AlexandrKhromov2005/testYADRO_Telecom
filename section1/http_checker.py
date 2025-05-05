import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

URLS = [
    'https://httpstat.us/200',
    'https://httpstat.us/201',
    'https://httpstat.us/302',
    'https://httpstat.us/404',
    'https://httpstat.us/500'
]

def check_urls():
    for url in URLS:
        try:
            response = requests.get(url, allow_redirects=False)
            status = response.status_code
            
            if 100 <= status < 400:
                logger.info(f"Success: {status}\nResponse Body: {response.text}")
            else:
                logger.error(f"HTTP Error: {status}\nResponse: {response.text}")  
                raise Exception(f"Critical HTTP Error: {status}")  

        except Exception as e:
            logger.error(f"Failed for {url}: {str(e)}")
            

if __name__ == "__main__":
    check_urls()