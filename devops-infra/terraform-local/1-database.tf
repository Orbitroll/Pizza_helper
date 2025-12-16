resource "kubernetes_deployment_v1" "postgres" {
  metadata {
    name = "postgres"
    namespace = kubernetes_namespace_v1.pizza_helper.metadata[0].name
  }

  spec {
    replicas = 1
    selector {
      match_labels = {
        app = "postgres"
      }
    }

    template {
      metadata {
        labels = {
          app = "postgres"
        }
      }

      spec {
        container {
          image = "postgres:15-alpine"
          name  = "postgres"

          env {
            name  = "POSTGRES_USER"
            value = "pizza_user"
          }
          env {
            name  = "POSTGRES_PASSWORD"
            value = "pizza_password"
          }
          env {
            name  = "POSTGRES_DB"
            value = "pizza_db"
          }

          port {
            container_port = 5432
          }
        }
      }
    }
  }
}

resource "kubernetes_service_v1" "postgres" {
  metadata {
    name      = "db"
    namespace = kubernetes_namespace_v1.pizza_helper.metadata[0].name
  }

  spec {
    selector = {
      app = "postgres"
    }

    port {
      port        = 5432
      target_port = 5432
    }

    type = "ClusterIP"
  }
}
