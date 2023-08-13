# Monitoring Web Application Response Time with Prometheus and Grafana

This repository contains a solution for monitoring the response time of a web application using Prometheus, Grafana, and a custom Prometheus exporter. The exporter measures the response time of the web application, exposes the metrics in Prometheus-compatible format, and enables real-time visualization through Grafana.

## Requirements

- Docker
- Docker Compose

## Components

1. **Web Application:** The web application under monitoring (for example, your own website or any other website).
2. **Prometheus Exporter:** A custom Prometheus exporter that measures the response time of the web application and exposes metrics.
3. **Prometheus:** Collects and stores metrics from exporters.
4. **Grafana:** A visualization tool for creating informative dashboards.

## Usage

1. **How to run solution:**
- Before running solution, if we need to update the website's name to check the performance, we can change the environment: [WEBSITE_URL](response_time_exporter/settings.py). I use by default with the Grafana domain: http://grafana-host:3000.

- In this solution, I will also provide some metrics including: response time, error code rate and http code status.

```
make build # Build apps
make run   # Run apps
make stop  # Stop apps
make clean # Clean apps
```
2. **Access Grafana:**

- Open your browser and navigate to http://localhost:3000.
```
Username: admin
Password: admin (You'll be prompted to change the password on first login)
```

3. **Add Prometheus Data Source in Grafana:**
- From the Grafana home page, click on the gear icon (⚙️) on the left sidebar to access the settings.
- Under "Configuration," click on "Data Sources."
Click "Add data source," select "Prometheus," and provide the URL (http://prometheus-host:9090).
   
4. **View and Analyze Metrics:**

- We can now explore the Grafana dashboard to visualize and analyze response time metrics.

![image](https://user-images.githubusercontent.com/28616641/260290901-1b9c4e8c-0432-48ef-9323-8ba9b4489014.png)

5. **Alerting:**

- We can also use Grafana Alerting for trigger metric over threshold.

![image](https://user-images.githubusercontent.com/28616641/260290897-a3c3bbb3-79e7-4623-a626-25bcfbb4e1e4.png)


