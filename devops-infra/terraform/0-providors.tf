terraform {
  required_providers {
    aws = {
        source = "hashicorp/aws"
        version = "~> 6.0"
    }
  }
  
  # Remote State Configuration (S3 + DynamoDB)
  # Note: The bucket and table must be created manually before running terraform init
  backend "s3" {
    bucket       = "pizza-helper-terraform-state" # Replace with your unique bucket name
    key          = "terraform.tfstate"
    region       = "us-east-1"
    use_lockfile = true
    encrypt      = true
  }
}
provider "aws" {
    region = var.aws_region
    
    default_tags {
      tags = {
        Environment = terraform.workspace
        Project     = "Pizza-Helper"
        ManagedBy   = "Terraform"
      }
    }
}

