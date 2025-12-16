terraform {
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = ">= 2.0.0"
    }
  }
}

provider "kubernetes" {
  host = "https://host.docker.internal:6443"
  insecure = true
}

resource "kubernetes_namespace" "pizza_helper" {
  metadata {
    name = "pizza-helper"
  }
}
