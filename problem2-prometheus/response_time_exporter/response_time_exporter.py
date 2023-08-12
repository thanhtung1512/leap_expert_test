from prometheus_client import start_http_server, Summary
import requests
import time

# Create a Summary metric to measure response times
response_time_summary = Summary('website_response_time_seconds', 'Website Response Time in seconds')

# URL of the website to monitor
website_url = 'https://google.com'

def monitor_website():
    while True:
        start_time = time.time()
        response = requests.get(website_url)
        response_time = time.time() - start_time

        # Record the response time metric
        response_time_summary.observe(response_time)

        time.sleep(60)  # Monitor every 60 seconds

if __name__ == '__main__':
    start_http_server(8000)  # Expose metrics for Prometheus scraping on port 8000
    monitor_website()
