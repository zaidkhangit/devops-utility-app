DevSecOps FastAPI Application

This repository contains a FastAPI-based backend integrated with a complete DevSecOps pipeline using Docker, GitHub Actions, and AWS. It also includes Kubernetes manifests for container orchestration and scaling.

Features

FastAPI backend with a modular structure separating routers and services.
Containerized application using Docker with support for Docker Compose.
Automated CI/CD pipelines using GitHub Actions for build, deployment, and security checks.
Integration with AWS services to monitor infrastructure.

The monitoring service fetches S3 buckets and EC2 instances, highlights resources older than 90 days, and detects newly created resources.

Local Development

Clone the repository and install dependencies:

git clone https://github.com/your-repo.git
cd your-repo
pip install -r requirements.txt

Run the application:

python main.py

Test locally:

curl http://localhost:8081
Kubernetes Deployment

Kubernetes manifests are available in the k8s directory.

The application runs internally on port 8081 and is exposed externally using a NodePort service on port 30081.

For local access using port forwarding:

kubectl port-forward service/<service-name> 8081:8081

For external access:

http://:30081

Secrets and Configuration

Secrets are managed using a secrets configuration file where AWS and Docker credentials must be provided in Base64 encoded format without spaces.

Non-sensitive configuration values are stored using ConfigMap.

Auto Scaling

Horizontal Pod Autoscaler is configured to automatically scale the application when CPU usage reaches or exceeds 70 percent.

Deployment

The CI/CD pipeline performs the following steps:

Builds the Docker image
Pushes the image to the container registry
Deploys the application to an EC2 instance using SSH and Docker Compose

After deployment, verify the service:

curl http://<ec2-ip>:8081
Security

Security scanning is integrated using Trivy for container images. Sensitive credentials are managed using GitHub Secrets and environment variables.

Summary

This project demonstrates a complete DevSecOps workflow including development, continuous integration, security scanning, deployment, infrastructure monitoring, and auto scaling.





