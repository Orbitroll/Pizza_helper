output "cluster_name" {
  description = "Kubernetes Cluster Name"
  value       = aws_eks_cluster.pizza_helper_cluster.name
}

output "cluster_endpoint" {
  description = "Endpoint for EKS control plane"
  value       = aws_eks_cluster.pizza_helper_cluster.endpoint
}

output "cluster_security_group_id" {
  description = "Security group ids attached to the cluster control plane"
  value       = aws_eks_cluster.pizza_helper_cluster.vpc_config[0].cluster_security_group_id
}

output "region" {
  description = "AWS region"
  value       = var.aws_region
}

output "ecr_backend_repository_url" {
  value = aws_ecr_repository.backend.repository_url
}

output "ecr_frontend_repository_url" {
  value = aws_ecr_repository.frontend.repository_url
}
