resource "aws_iam_role" "cluster" {
  name = "eks-cluster-example"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "sts:AssumeRole",
          "sts:TagSession"
        ]
        Effect = "Allow"
        Principal = {
          Service = "eks.amazonaws.com"
        }
      },
    ]
  })
}
resource "aws_iam_role_policy_attachment" "eks_cluter_policy_attachment" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
  role       = aws_iam_role.cluster.name
  
}
resource "aws_eks_cluster" "pizza_helper_cluster" {
  name     = "pizza-helper-cluster-${terraform.workspace}"
  role_arn = aws_iam_role.cluster.arn

  vpc_config {
    endpoint_private_access = true
    endpoint_public_access  = true
    subnet_ids = [
      aws_subnet.public_pizza_helper_subnet-1.id,
      aws_subnet.public_pizza_helper_subnet-2.id
    ]
  }
  access_config {
    authentication_mode = "API"
  }
  version = "1.34"

  depends_on = [
    aws_iam_role_policy_attachment.eks_cluter_policy_attachment
  ]
  tags = {
    Name = "Pizza-Helper-EKS-Cluster-${terraform.workspace}"
  }

  bootstrap_self_managed_addons = true
  upgrade_policy {
    support_type = "STANDARD"
  }
}

resource "aws_eks_addon" "ebs_csi_driver" {
  cluster_name = aws_eks_cluster.pizza_helper_cluster.name
  addon_name   = "aws-ebs-csi-driver"
  addon_version = "v1.35.0-eksbuild.1" # You might need to adjust this version based on your K8s version
}