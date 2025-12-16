terraform {
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = ">= 2.0.0"
    }
  }
}

variable "kube_config" {
  type    = string
  default = "~/.kube/config"
}

provider "kubernetes" {
  config_path = var.kube_config
}

resource "kubernetes_namespace_v1" "pizza_helper" {
  metadata {
    name = "pizza-helper"
  }
}
