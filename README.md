# Pizza Helper Project

This project is a full-stack web application with a complete DevOps infrastructure including Kubernetes, Terraform, and Jenkins. It supports both AWS Cloud deployment and a fully local development environment using Docker Desktop.

## Project Structure

```
pizza-helper/
├── app/                    # Application Source Code
│   ├── frontend/           # React/Vite Frontend
│   └── backend/            # Python/Flask Backend
├── devops-infra/           # DevOps Infrastructure
│   ├── jenkins/            # Jenkins CI/CD Pipeline (Local & Cloud)
│   ├── terraform/          # Terraform for AWS
│   └── terraform-local/    # Terraform for Local Kubernetes
├── .env.example            # Example Environment Variables
└── README.md               # This file
```

## Environment Configuration

Create a `.env` file in the root directory based on `.env.example`:

```bash
cp .env.example .env
```

**Required Variables:**
*   `POSTGRES_USER`: Database username
*   `POSTGRES_PASSWORD`: Database password
*   `POSTGRES_DB`: Database name
*   `DATABASE_URL`: Connection string for the backend
*   `FLASK_ENV`: Backend environment (development/production)

## Local Development Environment

We use a local Kubernetes setup with Jenkins and Terraform to simulate a real DevOps workflow.

### 1. Prerequisites
*   Docker Desktop (with Kubernetes enabled)
*   Git

### 2. Start Jenkins
Run the custom Jenkins container which includes Terraform and Kubectl:

```bash
cd devops-infra/jenkins
docker build -t my-jenkins-tools .
docker run -d --name jenkins-local -p 3711:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home -v //var/run/docker.sock:/var/run/docker.sock my-jenkins-tools
```
Access Jenkins at: `http://localhost:3711`

### 3. Jenkins Pipelines
We have a unified CI/CD pipeline and a cleanup pipeline:

*   **CI/CD Pipeline** (`Jenkinsfile.ci_cd`):
    *   Triggered by GitHub push (if commit message contains "deploy").
    *   Tests Backend & Frontend.
    *   Builds & Pushes Docker Images.
    *   Deploys to Local Kubernetes using Terraform.
*   **Destroy Pipeline** (`Jenkinsfile.destroy`):
    *   Destroys all resources created by Terraform.

### 4. Cleanup
To destroy all environments and clean up resources, use the **Destroy Pipeline** (`Jenkinsfile.destroy`).

## Infrastructure (Terraform)

The infrastructure is managed using Terraform.
*   **Local**: `devops-infra/terraform-local/` (Uses Kubernetes Provider)
*   **AWS**: `devops-infra/terraform/` (Uses AWS Provider - EKS, VPC, ECR)

## Application

The application consists of a React frontend and a Flask backend.
*   **Frontend**: Runs on port 80 (via Nginx) inside the cluster.
*   **Backend**: Runs on port 5000 (via Gunicorn) inside the cluster.
