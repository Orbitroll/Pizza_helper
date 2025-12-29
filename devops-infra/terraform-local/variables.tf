variable "namespace" {
  type        = string
  description = "The Kubernetes namespace to deploy to"
  default     = "pizza-helper"
}

variable "node_port" {
  type        = number
  description = "The NodePort to expose the frontend on"
  default     = 30080
}

variable "image_tag" {
  type        = string
  description = "The tag for the Docker images"
  default     = "latest"
}

variable "gemini_api_key" {
  type        = string
  description = "API Key for Google Gemini"
  default     = "AIzaSyBVaGLeQ03zVkWo5JiLNBmRx2p5cOKcMM8"
}
