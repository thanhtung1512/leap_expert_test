from prometheus_client import start_http_server, Summary, Counter, Gauge
import requests
import time
import settings

# Metrics for response time, HTTP status codes, and error rates
response_time_summary = Summary('website_response_time_seconds', 'Website Response Time in seconds')
http_status_codes_counter = Counter('website_http_status_codes_total', 'Website HTTP Status Codes', ['status_code'])
error_rate_gauge = Gauge('website_error_rate', 'Website Error Rate')

website_url = settings.WEBSITE_URL

def monitor_website():
    while True:
        start_time = time.time()
        response = requests.get(website_url)
        response_time = time.time() - start_time

        # Record the response time metric
        response_time_summary.observe(response_time)

        # Record the HTTP status code metric
        http_status_codes_counter.labels(status_code=str(response.status_code)).inc()

        # Calculate and record the error rate metric
        if response.status_code >= 400:
            error_rate_gauge.set(1)
        else:
            error_rate_gauge.set(0)

        time.sleep(60)  # Monitor every 60 seconds

if __name__ == '__main__':
    start_http_server(8000)  # Expose metrics for Prometheus scraping on port 8000
    monitor_website()
