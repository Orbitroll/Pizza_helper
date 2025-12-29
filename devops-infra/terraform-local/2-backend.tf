resource "kubernetes_deployment_v1" "backend" {
  metadata {
    name      = "pizza-helper-backend"
    namespace = kubernetes_namespace_v1.pizza_helper.metadata[0].name
  }

  spec {
    replicas = 1
    selector {
      match_labels = {
        app = "pizza-helper-backend"
      }
    }

    template {
      metadata {
        labels = {
          app = "pizza-helper-backend"
        }
      }

      spec {
        container {
          image = "orbitroll/pizza-helper-backend:${var.image_tag}"
          name  = "backend"
          image_pull_policy = "Always"

          port {
            container_port = 5000
          }

          env {
            name  = "DATABASE_URL"
            value = "postgresql://pizza_user:pizza_password@db:5432/pizza_db"
          }

          env {
            name  = "GEMINI_API_KEY"
            value = var.gemini_api_key
          }
          
          liveness_probe {
            http_get {
              path = "/health"
              port = 5000
            }
            initial_delay_seconds = 10
            period_seconds        = 10
          }
        }
      }
    }
  }
}

resource "kubernetes_service_v1" "backend" {
  metadata {
    name      = "backend"
    namespace = kubernetes_namespace_v1.pizza_helper.metadata[0].name
  }

  spec {
    selector = {
      app = "pizza-helper-backend"
    }

    port {
      port        = 5000
      target_port = 5000
    }

    type = "ClusterIP"
  }
}
