# Setting Up Grafana Using Docker

Setting up Grafana locally using Docker is a straightforward process. Docker simplifies the installation and running of Grafana, allowing you to get your Grafana instance up and running quickly. Here are the steps to do so:

## Steps to Setup Grafana Using Docker

### 1. Pull the Grafana Docker Image

First, you need to pull the official Grafana Docker image from Docker Hub. Open your terminal and run the following command:

```bash
docker pull grafana/grafana
```

### 2. Run Grafana in a Docker Container

After pulling the image, you can run Grafana in a new Docker container. Use the following command:

```bash
docker run -d -p 3000:3000 --name=grafana grafana/grafana
```

Here's what this command does:

- `-d` runs the container in detached mode (in the background).
- `-p 3000:3000` maps port 3000 on the host to port 3000 in the container, which is the default port that Grafana runs on.
- `--name=grafana` names the container 'grafana'.
- `grafana/grafana` is the name of the image to run.


```bash
docker run -d -p 3000:3000 --net=host --name=grafana grafana/grafana
```

### 3. Accessing Grafana

Once the Grafana container is running, you can access the Grafana UI in your web browser:

```
http://localhost:3000
```

### 4. Login to Grafana

By default, Grafana will have the following credentials:

- Username: admin
- Password: admin

Upon first login, Grafana will prompt you to change the default password.

### 5. Configure Data Sources and Dashboards

Once logged in, you can start configuring Grafana:

- Add Data Sources: Add data sources like Prometheus, MySQL, Elasticsearch, etc., that Grafana will use to pull metrics or logs.
- Create Dashboards: Create and configure dashboards to visualize the data from your data sources.

### 6. Additional Configurations (Optional)

If you need to customize your Grafana instance, like configuring SMTP settings, you can pass environment variables to the Docker container using the `-e` flag. For example:

```bash
docker run -d -p 3000:3000 -e "GF_SMTP_ENABLED=true" -e "GF_SMTP_HOST=smtp.example.com" --name=grafana grafana/grafana
```

### 7. Persistent Storage (Optional)

To make Grafana data (like dashboards and configurations) persistent, you can mount a volume to the Docker container. This is useful when you want your data to persist even after the container is stopped or deleted.

```bash
docker run -d -p 3000:3000 -v grafana-storage:/var/lib/grafana --name=grafana grafana/grafana
```

Here, grafana-storage is the name of the Docker volume that will store Grafana's data.


# Setting Up Prometheus Using Docker

Prometheus is an open-source monitoring system with a dimensional data model, flexible query language, efficient time series database, and modern alerting approach. Using Docker to run Prometheus makes the setup process straightforward and easy to maintain.

## Steps

### 1. Pull Prometheus Docker Image

First, you need to pull the official Prometheus Docker image from Docker Hub.

```bash
docker pull prom/prometheus
```

This command downloads the latest Prometheus image to your local machine.

### 2. Create a Prometheus Configuration File

Prometheus requires a configuration file (usually named prometheus.yml). You can start with a basic configuration.

Create a file prometheus.yml with the following content:

```yaml
global:
  scrape_interval: 15s  # By default, scrape targets every 15 seconds.

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']  # Scrape the Prometheus instance itself.
```

This configuration tells Prometheus to scrape metrics from itself (localhost:9090) every 15 seconds.

### 3. Run Prometheus in a Docker Container

Run a Docker container with the Prometheus image, binding the configuration file:

```bash
docker run -d -p 9090:9090 -v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml --name=prometheus prom/prometheus
```

Explanation of the command:

- `-d` runs the container in detached mode.
- `-p 9090:9090` exposes Prometheus on port 9090 on your local machine.
- `-v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml` mounts your local `prometheus.yml` file into the container.
- `--name=prometheus` gives your container a recognizable name.
- `prom/prometheus` is the name of the Docker image.

For network configuration:

```bash
sudo docker run -d -p 9090:9090 --net=host -v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml --name=prometheus prom/prometheus
```

### 4. Accessing Prometheus

You can access the Prometheus web UI by navigating to:

```
http://localhost:9090
```

Here, you can execute Prometheus queries to explore your metrics.

### 1. Executing Basic Queries

- **Query Bar**: On the main dashboard, there's a query bar at the top.
- **Entering a Metric**: Input a metric name to retrieve its current value. For example, if your Flask application exposes `http_requests_total`, enter this into the query bar.
- **Execution and Visualization**: After typing the metric name, press `Execute`. To view the metric's trend over time, click on the `Graph` tab.

### 2. Viewing All Metrics

- **Graph Menu**: Click on the `Graph` menu item to explore metrics.
- **Discovering Metrics**: In the query bar, start typing to see auto-complete suggestions of available metrics. This feature helps in quickly finding and selecting the metrics you're interested in.

### Additional Tips

- **Exploring Data**: Prometheus's web UI is a powerful tool to explore the data it's collecting. You can use it to debug issues, understand system behavior, or simply learn more about the metrics being collected.
- **Advanced Queries**: As you become more familiar with Prometheus, you can use its query language, PromQL, to write more complex queries for in-depth analysis.

### 5. Stopping and Restarting Prometheus

To stop your Prometheus Docker container:

```bash
docker stop prometheus
```

To start it again:

```bash
docker start prometheus
```

