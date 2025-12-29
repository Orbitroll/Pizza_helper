import json
import os

def create_panel(id, title, query, type="timeseries", unit="short", gridPos={"h": 8, "w": 12, "x": 0, "y": 0}):
    panel = {
        "id": id,
        "title": title,
        "type": type,
        "gridPos": gridPos,
        "targets": [
            {
                "expr": query,
                "refId": "A"
            }
        ],
        "datasource": "prometheus",
        "fieldConfig": {
            "defaults": {
                "unit": unit,
                "color": {"mode": "palette-classic"},
            },
            "overrides": []
        }
    }
    
    if type == "timeseries":
        panel["fieldConfig"]["defaults"]["custom"] = {
            "drawStyle": "line",
            "lineInterpolation": "smooth",
            "showPoints": "auto",
            "lineWidth": 2,
            "fillOpacity": 10,
            "gradientMode": "opacity",
            "axisCenteredZero": False,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "hideFrom": {
              "legend": False,
              "tooltip": False,
              "viz": False
            },
            "scaleDistribution": {
              "type": "linear"
            },
            "showValues": "never",
            "spanNulls": False,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
        }
        panel["options"] = {
            "legend": {
                "calcs": [],
                "displayMode": "list",
                "placement": "bottom",
                "showLegend": True
            },
            "tooltip": {
                "mode": "single",
                "sort": "none"
            }
        }
    
    elif type == "stat":
        panel["options"] = {
            "reduceOptions": {
                "values": False,
                "calcs": ["lastNotNull"],
                "fields": ""
            },
            "orientation": "auto",
            "textMode": "auto",
            "colorMode": "value",
            "graphMode": "area",
            "justifyMode": "auto"
        }
        # Add thresholds for stat panels
        panel["fieldConfig"]["defaults"]["thresholds"] = {
            "mode": "absolute",
            "steps": [
                {"color": "green", "value": 0},
                {"color": "red", "value": 1} if "Unhealthy" in title or "Error" in title else {"color": "orange", "value": 5}
            ]
        }
        
    return panel

def create_row(id, title, gridPos={"h": 1, "w": 24, "x": 0, "y": 0}):
    return {
        "id": id,
        "title": title,
        "type": "row",
        "gridPos": gridPos,
        "collapsed": False,
        "panels": []
    }

def create_dashboard(uid, title, panels):
    return {
        "annotations": {
            "list": [
                {
                    "builtIn": 1,
                    "datasource": "-- Grafana --",
                    "enable": True,
                    "hide": True,
                    "iconColor": "rgba(0, 211, 255, 1)",
                    "name": "Annotations & Alerts",
                    "type": "dashboard"
                }
            ]
        },
        "editable": True,
        "gnetId": None,
        "graphTooltip": 0,
        "id": None,
        "links": [],
        "panels": panels,
        "schemaVersion": 27,
        "style": "dark",
        "tags": ["kubernetes", "pizza-helper"],
        "templating": {
            "list": []
        },
        "time": {
            "from": "now-1h",
            "to": "now"
        },
        "timepicker": {
            "refresh_intervals": [
                "5s", "10s", "30s", "1m", "5m", "15m", "30m", "1h", "2h", "1d"
            ]
        },
        "timezone": "",
        "title": title,
        "uid": uid,
        "version": 1
    }

# Flask Dashboard
flask_panels = []
id_counter = 1
y_pos = 0

flask_queries = [
    ("Total Requests per Second", 'sum(rate(flask_http_request_total[5m]))', "reqps"),
    ("Requests per Second by Status Code", 'sum(rate(flask_http_request_total[5m])) by (status)', "reqps"),
    ("Requests per Second by Endpoint", 'sum(rate(flask_http_request_total[5m])) by (path)', "reqps"),
    ("Global Error Rate (5xx)", 'sum(rate(flask_http_request_total{status=~"5.."}[5m]))', "reqps"),
    ("Error Rate by Endpoint", 'sum(rate(flask_http_request_total{status=~"5.."}[5m])) by (path)', "reqps"),
    ("Average Request Duration", 'rate(flask_http_request_duration_seconds_sum[5m]) / rate(flask_http_request_duration_seconds_count[5m])', "s"),
    ("95th Percentile Latency", 'histogram_quantile(0.95, sum(rate(flask_http_request_duration_seconds_bucket[5m])) by (le))', "s"),
    ("99th Percentile Latency", 'histogram_quantile(0.99, sum(rate(flask_http_request_duration_seconds_bucket[5m])) by (le))', "s")
]

for i, (title, query, unit) in enumerate(flask_queries):
    x_pos = (i % 2) * 12
    if i > 0 and i % 2 == 0:
        y_pos += 8
    flask_panels.append(create_panel(id_counter, title, query, "timeseries", unit, {"h": 8, "w": 12, "x": x_pos, "y": y_pos}))
    id_counter += 1

flask_dashboard = create_dashboard("pizza-helper-flask", "Pizza Helper Flask Dashboard", flask_panels)

# Kubernetes Dashboard
k8s_panels = []
id_counter = 100
y_pos = 0

# Frontend & DB
k8s_panels.append(create_row(id_counter, "Frontend (Nginx) & Database (Postgres)", {"h": 1, "w": 24, "x": 0, "y": y_pos}))
id_counter += 1
y_pos += 1

frontend_db_queries = [
    ("Frontend CPU Usage", 'sum(rate(container_cpu_usage_seconds_total{namespace="pizza-helper", pod=~"pizza-helper-frontend.*"}[5m]))', "short"),
    ("Frontend Memory Usage", 'sum(container_memory_usage_bytes{namespace="pizza-helper", pod=~"pizza-helper-frontend.*"})', "bytes"),
    ("Database CPU Usage", 'sum(rate(container_cpu_usage_seconds_total{namespace="pizza-helper", pod=~"postgres.*"}[5m]))', "short"),
    ("Database Memory Usage", 'sum(container_memory_usage_bytes{namespace="pizza-helper", pod=~"postgres.*"})', "bytes")
]

for i, (title, query, unit) in enumerate(frontend_db_queries):
    x_pos = (i % 2) * 12
    if i > 0 and i % 2 == 0:
        y_pos += 8
    k8s_panels.append(create_panel(id_counter, title, query, "timeseries", unit, {"h": 8, "w": 12, "x": x_pos, "y": y_pos}))
    id_counter += 1

y_pos += 8

# Infrastructure
k8s_panels.append(create_row(id_counter, "Kubernetes Infrastructure (All Pods)", {"h": 1, "w": 24, "x": 0, "y": y_pos}))
id_counter += 1
y_pos += 1

infra_queries = [
    ("CPU Usage by Pod (Cores)", 'sum(rate(container_cpu_usage_seconds_total{namespace="pizza-helper"}[5m])) by (pod)', "short"),
    ("Total CPU Usage in Namespace", 'sum(rate(container_cpu_usage_seconds_total{namespace="pizza-helper"}[5m]))', "short"),
    ("Memory Usage by Pod (Bytes)", 'sum(container_memory_usage_bytes{namespace="pizza-helper"}) by (pod)', "bytes"),
    ("Network Receive Rate (Bytes/sec)", 'sum(rate(container_network_receive_bytes_total{namespace="pizza-helper"}[5m])) by (pod)', "Bps"),
    ("Network Transmit Rate (Bytes/sec)", 'sum(rate(container_network_transmit_bytes_total{namespace="pizza-helper"}[5m])) by (pod)', "Bps"),
    ("Pod Restarts (Last 1 hour)", 'sum(changes(kube_pod_container_status_restarts_total{namespace="pizza-helper"}[1h])) by (pod)', "short"),
    ("Unhealthy Pods (Not Ready)", 'count(kube_pod_status_ready{condition="true", namespace="pizza-helper"} == 0)', "short")
]

for i, (title, query, unit) in enumerate(infra_queries):
    x_pos = (i % 2) * 12
    if i > 0 and i % 2 == 0:
        y_pos += 8
    
    panel_type = "timeseries"
    if "Restarts" in title or "Unhealthy" in title:
        panel_type = "stat"
        
    k8s_panels.append(create_panel(id_counter, title, query, panel_type, unit, {"h": 8, "w": 12, "x": x_pos, "y": y_pos}))
    id_counter += 1

k8s_dashboard = create_dashboard("pizza-helper-k8s", "Pizza Helper Kubernetes Dashboard", k8s_panels)

# Save files
output_dir = "devops-infra/monitoring/grafana/dashboards"
os.makedirs(output_dir, exist_ok=True)

with open(os.path.join(output_dir, "flask-dashboard.json"), "w") as f:
    json.dump(flask_dashboard, f, indent=2)

with open(os.path.join(output_dir, "kubernetes-dashboard.json"), "w") as f:
    json.dump(k8s_dashboard, f, indent=2)

print("Dashboards generated successfully.")
