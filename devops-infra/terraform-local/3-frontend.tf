resource "kubernetes_deployment_v1" "frontend" {
  metadata {
    name      = "pizza-helper-frontend"
    namespace = kubernetes_namespace_v1.pizza_helper.metadata[0].name
  }

  spec {
    replicas = 1
    selector {
      match_labels = {
        app = "pizza-helper-frontend"
      }
    }

    template {
      metadata {
        labels = {
          app = "pizza-helper-frontend"
        }
      }

      spec {
        container {
          image = "orbitroll/pizza-helper-frontend:${var.image_tag}"
          name  = "frontend"
          image_pull_policy = "Always"

          port {
            container_port = 80
          }
        }
      }
    }
  }
}

resource "kubernetes_service_v1" "frontend" {
  metadata {
    name      = "pizza-helper-frontend"
    namespace = kubernetes_namespace_v1.pizza_helper.metadata[0].name
  }

  spec {
    selector = {
      app = "pizza-helper-frontend"
    }

    port {
      port        = 80
      target_port = 80
    }

    type = "LoadBalancer"
  }
}
