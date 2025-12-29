# Prometheus Queries for Pizza Helper

This document contains useful PromQL queries for monitoring the Pizza Helper application and the Kubernetes infrastructure.

## Backend Application (Flask)

These queries assume the backend is instrumented with `prometheus-flask-exporter`.

### Traffic
**Total Requests per Second**
```promql
sum(rate(flask_http_request_total[5m]))
```

**Requests per Second by Status Code**
```promql
sum(rate(flask_http_request_total[5m])) by (status)
```

**Requests per Second by Endpoint**
```promql
sum(rate(flask_http_request_total[5m])) by (path)
```

### Errors
**Global Error Rate (5xx)**
```promql
sum(rate(flask_http_request_total{status=~"5.."}[5m]))
```

**Error Rate by Endpoint**
```promql
sum(rate(flask_http_request_total{status=~"5.."}[5m])) by (path)
```

### Latency / Performance
**Average Request Duration**
```promql
rate(flask_http_request_duration_seconds_sum[5m]) / rate(flask_http_request_duration_seconds_count[5m])
```

**95th Percentile Latency**
```promql
histogram_quantile(0.95, sum(rate(flask_http_request_duration_seconds_bucket[5m])) by (le))
```

**99th Percentile Latency**
```promql
histogram_quantile(0.99, sum(rate(flask_http_request_duration_seconds_bucket[5m])) by (le))
```

## Frontend (Nginx) & Database (Postgres)

Since these are not instrumented with native Prometheus exporters in this setup, we monitor them via their **Pod metrics**.

### Frontend Pods
**CPU Usage**
```promql
sum(rate(container_cpu_usage_seconds_total{namespace="pizza-helper", pod=~"pizza-helper-frontend.*"}[5m]))
```

**Memory Usage**
```promql
sum(container_memory_usage_bytes{namespace="pizza-helper", pod=~"pizza-helper-frontend.*"})
```

### Database Pods
**CPU Usage**
```promql
sum(rate(container_cpu_usage_seconds_total{namespace="pizza-helper", pod=~"postgres.*"}[5m]))
```

**Memory Usage**
```promql
sum(container_memory_usage_bytes{namespace="pizza-helper", pod=~"postgres.*"})
```

---

## Kubernetes Infrastructure (All Pods)

### CPU Usage
**CPU Usage by Pod (Cores)**
```promql
sum(rate(container_cpu_usage_seconds_total{namespace="pizza-helper"}[5m])) by (pod)
```

**Total CPU Usage in Namespace**
```promql
sum(rate(container_cpu_usage_seconds_total{namespace="pizza-helper"}[5m]))
```

### Memory Usage
**Memory Usage by Pod (Bytes)**
```promql
sum(container_memory_usage_bytes{namespace="pizza-helper"}) by (pod)
```

### Network
**Network Receive Rate (Bytes/sec)**
```promql
sum(rate(container_network_receive_bytes_total{namespace="pizza-helper"}[5m])) by (pod)
```

**Network Transmit Rate (Bytes/sec)**
```promql
sum(rate(container_network_transmit_bytes_total{namespace="pizza-helper"}[5m])) by (pod)
```

### Health & Availability
**Pod Restarts (Last 1 hour)**
```promql
sum(changes(kube_pod_container_status_restarts_total{namespace="pizza-helper"}[1h])) by (pod)
```

**Unhealthy Pods (Not Ready)**
```promql
count(kube_pod_status_ready{condition="true", namespace="pizza-helper"} == 0)
```
