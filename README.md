# shlomis Project

# Pizza Helper Project

This project is a full-stack web application with a complete DevOps infrastructure including Kubernetes, Terraform, and Jenkins.

## Project Structure

```
pizza-helper/
├── app/                    # Application Source Code
│   ├── frontend/           # React/Vite Frontend
│   └── backend/            # Python/Flask Backend
├── devops-infra/           # DevOps Infrastructure
│   ├── jenkins/            # Jenkins CI/CD Pipeline
│   ├── kubernetes/         # Kubernetes Manifests (Deployment, Service, Ingress)
│   └── terraform/          # Infrastructure as Code (AWS EKS, VPC, ECR)
└── README.md               # This file
```

## Infrastructure (Terraform)

The infrastructure is managed using Terraform and includes:
- **VPC**: Custom networking.
- **EKS Cluster**: Managed Kubernetes.
- **ECR**: Container registries.
- **State Management**: S3 Backend with Locking.

See [devops-infra/terraform/README.md](devops-infra/terraform/README.md) for setup instructions.

## CI/CD (Jenkins)

The pipeline is defined in `devops-infra/jenkins/Jenkinsfile` and handles:
1.  **Test**: Runs unit tests for Frontend and Backend.
2.  **Build**: Builds Docker images.
3.  **Push**: Pushes images to Docker Hub (or ECR).
4.  **Deploy**: Deploys to EKS using `kubectl`.

## Getting Started

1.  **Infrastructure**:
    Navigate to `devops-infra/terraform` and follow the README to provision AWS resources.

2.  **Application**:
    The application consists of a React frontend and a Flask backend.
    *   Frontend runs on port 80 (via Nginx).
    *   Backend runs on port 5000 (via Gunicorn).

## Development

*   **Frontend**: `cd app/frontend && npm install && npm run dev`
*   **Backend**: `cd app/backend && pip install -r requirements.txt && python app.py`
