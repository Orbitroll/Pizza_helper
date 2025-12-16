resource "kubernetes_deployment" "frontend" {
  metadata {
    name      = "pizza-helper-frontend"
    namespace = kubernetes_namespace.pizza_helper.metadata[0].name
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
          image = "orbitroll/pizza-helper-frontend:latest"
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

resource "kubernetes_service" "frontend" {
  metadata {
    name      = "pizza-helper-frontend"
    namespace = kubernetes_namespace.pizza_helper.metadata[0].name
  }

  spec {
    selector = {
      app = "pizza-helper-frontend"
    }

    port {
      port        = 80
      target_port = 80
      node_port   = 30080
    }

    type = "NodePort"
  }
}
