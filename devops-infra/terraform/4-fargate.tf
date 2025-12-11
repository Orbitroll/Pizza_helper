resource "aws_iam_role" "fargate_pod_execution_role" {
  name = "fargate-pod-execution-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "eks-fargate-pods.amazonaws.com"
        }
      },
    ]
  })
  
}
resource "aws_iam_role_policy_attachment" "fargate_pod_execution_role_policy_attachment" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSFargatePodExecutionRolePolicy"
  role       = aws_iam_role.fargate_pod_execution_role.name
  
}
resource "aws_eks_fargate_profile" "fargate-pizza-helper" {
    cluster_name = aws_eks_cluster.pizza_helper_cluster.name
    fargate_profile_name = "fargate-pizza-helper-profile"
    pod_execution_role_arn = aws_iam_role.fargate_pod_execution_role.arn
    
    subnet_ids = [
        aws_subnet.public_pizza_helper_subnet-1.id,
        aws_subnet.public_pizza_helper_subnet-2.id,
        aws_subnet.privete_pizza_helper_subnet-1.id,
        aws_subnet.privete_pizza_helper_subnet-2.id
    ]
    
    selector {
        namespace = "default"
    }
    
    depends_on = [
        aws_iam_role_policy_attachment.fargate_pod_execution_role_policy_attachment
    ]               
}
  
