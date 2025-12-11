# Pizza Helper Terraform Infrastructure

This directory contains the Terraform configuration for the Pizza Helper application infrastructure on AWS.

## Prerequisites

Before running Terraform, you must manually create the following AWS resources for remote state management:

1.  **S3 Bucket**: `pizza-helper-terraform-state` (or update `0-providors.tf` with your bucket name).
    *   Ensure versioning is enabled.

## Workspaces

This project uses Terraform Workspaces to manage different environments (e.g., `dev`, `prod`).

### Usage

1.  **Initialize Terraform**:
    ```bash
    terraform init
    ```

2.  **Create/Select a Workspace**:
    *   For Development:
        ```bash
        terraform workspace new dev
        terraform workspace select dev
        ```
    *   For Production:
        ```bash
        terraform workspace new prod
        terraform workspace select prod
        ```

3.  **Plan and Apply**:
    ```bash
    terraform plan
    terraform apply
    ```

## Resources Created

*   **VPC**: Custom VPC with public subnets.
*   **EKS Cluster**: Managed Kubernetes cluster.
*   **Fargate Profile**: Serverless compute for Kubernetes pods.
*   **Node Group**: Managed EC2 worker nodes.
*   **ECR Repositories**: Docker registries for Frontend and Backend.

## Outputs

After applying, Terraform will output:
*   `cluster_endpoint`: The EKS cluster API endpoint.
*   `cluster_name`: The name of the EKS cluster.
*   `ecr_repository_frontend_url`: URL for the Frontend ECR repo.
*   `ecr_repository_backend_url`: URL for the Backend ECR repo.
