import json

def create_panel(id, title, query, type="graph", gridPos={"h": 8, "w": 12, "x": 0, "y": 0}):
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
        "datasource": "prometheus"
    }
    if type == "stat":
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

dashboard = {
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
  "panels": [],
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
      "5s",
      "10s",
      "30s",
      "1m",
      "5m",
      "15m",
      "30m",
      "1h",
      "2h",
      "1d"
    ]
  },
  "timezone": "",
  "title": "Pizza Helper Kubernetes Dashboard",
  "uid": "pizza-helper-k8s",
  "version": 1
}

panels = []
id_counter = 1
y_pos = 0

# Backend Application (Flask)
panels.append(create_row(id_counter, "Backend Application (Flask)", {"h": 1, "w": 24, "x": 0, "y": y_pos}))
id_counter += 1
y_pos += 1

backend_queries = [
    ("Total Requests per Second", 'sum(rate(flask_http_request_total[5m]))'),
    ("Requests per Second by Status Code", 'sum(rate(flask_http_request_total[5m])) by (status)'),
    ("Requests per Second by Endpoint", 'sum(rate(flask_http_request_total[5m])) by (path)'),
    ("Global Error Rate (5xx)", 'sum(rate(flask_http_request_total{status=~"5.."}[5m]))'),
    ("Error Rate by Endpoint", 'sum(rate(flask_http_request_total{status=~"5.."}[5m])) by (path)'),
    ("Average Request Duration", 'rate(flask_http_request_duration_seconds_sum[5m]) / rate(flask_http_request_duration_seconds_count[5m])'),
    ("95th Percentile Latency", 'histogram_quantile(0.95, sum(rate(flask_http_request_duration_seconds_bucket[5m])) by (le))'),
    ("99th Percentile Latency", 'histogram_quantile(0.99, sum(rate(flask_http_request_duration_seconds_bucket[5m])) by (le))')
]

for i, (title, query) in enumerate(backend_queries):
    x_pos = (i % 2) * 12
    if i > 0 and i % 2 == 0:
        y_pos += 8
    panels.append(create_panel(id_counter, title, query, "graph", {"h": 8, "w": 12, "x": x_pos, "y": y_pos}))
    id_counter += 1

y_pos += 8

# Frontend (Nginx) & Database (Postgres)
panels.append(create_row(id_counter, "Frontend (Nginx) & Database (Postgres)", {"h": 1, "w": 24, "x": 0, "y": y_pos}))
id_counter += 1
y_pos += 1

frontend_db_queries = [
    ("Frontend CPU Usage", 'sum(rate(container_cpu_usage_seconds_total{namespace="pizza-helper", pod=~"pizza-helper-frontend.*"}[5m]))'),
    ("Frontend Memory Usage", 'sum(container_memory_usage_bytes{namespace="pizza-helper", pod=~"pizza-helper-frontend.*"})'),
    ("Database CPU Usage", 'sum(rate(container_cpu_usage_seconds_total{namespace="pizza-helper", pod=~"postgres.*"}[5m]))'),
    ("Database Memory Usage", 'sum(container_memory_usage_bytes{namespace="pizza-helper", pod=~"postgres.*"})')
]

for i, (title, query) in enumerate(frontend_db_queries):
    x_pos = (i % 2) * 12
    if i > 0 and i % 2 == 0:
        y_pos += 8
    panels.append(create_panel(id_counter, title, query, "graph", {"h": 8, "w": 12, "x": x_pos, "y": y_pos}))
    id_counter += 1

y_pos += 8

# Kubernetes Infrastructure (All Pods)
panels.append(create_row(id_counter, "Kubernetes Infrastructure (All Pods)", {"h": 1, "w": 24, "x": 0, "y": y_pos}))
id_counter += 1
y_pos += 1

infra_queries = [
    ("CPU Usage by Pod (Cores)", 'sum(rate(container_cpu_usage_seconds_total{namespace="pizza-helper"}[5m])) by (pod)'),
    ("Total CPU Usage in Namespace", 'sum(rate(container_cpu_usage_seconds_total{namespace="pizza-helper"}[5m]))'),
    ("Memory Usage by Pod (Bytes)", 'sum(container_memory_usage_bytes{namespace="pizza-helper"}) by (pod)'),
    ("Network Receive Rate (Bytes/sec)", 'sum(rate(container_network_receive_bytes_total{namespace="pizza-helper"}[5m])) by (pod)'),
    ("Network Transmit Rate (Bytes/sec)", 'sum(rate(container_network_transmit_bytes_total{namespace="pizza-helper"}[5m])) by (pod)'),
    ("Pod Restarts (Last 1 hour)", 'sum(changes(kube_pod_container_status_restarts_total{namespace="pizza-helper"}[1h])) by (pod)'),
    ("Unhealthy Pods (Not Ready)", 'count(kube_pod_status_ready{condition="true", namespace="pizza-helper"} == 0)')
]

for i, (title, query) in enumerate(infra_queries):
    x_pos = (i % 2) * 12
    if i > 0 and i % 2 == 0:
        y_pos += 8
    
    panel_type = "graph"
    if "Restarts" in title or "Unhealthy" in title:
        panel_type = "stat"
        
    panels.append(create_panel(id_counter, title, query, panel_type, {"h": 8, "w": 12, "x": x_pos, "y": y_pos}))
    id_counter += 1

dashboard["panels"] = panels

with open("devops-infra/monitoring/grafana/dashboards/kubernetes-dashboard.json", "w") as f:
    json.dump(dashboard, f, indent=2)

print("Dashboard generated successfully.")
