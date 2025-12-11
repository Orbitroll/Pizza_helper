resource "aws_iam_role" "eks_nodegroup_role" {
  name = "eks-nodegroup-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "ec2.amazonaws.com"
        }
      },
    ]
  })
  
}
resource "aws_iam_role_policy_attachment" "eks_nodegroup_role_policy_attachment" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy"
  role       = aws_iam_role.eks_nodegroup_role.name

  
}
resource "aws_iam_role_policy_attachment" "eks_cni_policy_attachment" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy"
  role       = aws_iam_role.eks_nodegroup_role.name
  
}
resource "aws_iam_role_policy_attachment" "eks_registry_policy_attachment" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
  role       = aws_iam_role.eks_nodegroup_role.name
  
}
resource "aws_eks_node_group" "pizza_helper_nodegroup" {
  cluster_name    = aws_eks_cluster.pizza_helper_cluster.name
  node_group_name = "pizza-helper-nodegroup"
  node_role_arn   = aws_iam_role.eks_nodegroup_role.arn
  subnet_ids = [
    aws_subnet.public_pizza_helper_subnet-1.id,
    aws_subnet.public_pizza_helper_subnet-2.id
  ]
  scaling_config {
    desired_size = 2
    max_size     = 3
    min_size     = 1
  }
  instance_types = ["t3.medium"]
  ami_type       = "AL2_x86_64"
  disk_size      = 20

  depends_on = [
    aws_iam_role_policy_attachment.eks_nodegroup_role_policy_attachment,
    aws_iam_role_policy_attachment.eks_cni_policy_attachment,
    aws_iam_role_policy_attachment.eks_registry_policy_attachment
  ]
  tags = {
    Name = "Pizza-Helper-EKS-Nodegroup"
  }
}