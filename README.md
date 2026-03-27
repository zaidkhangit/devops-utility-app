DevSecOps FastAPI Application

This repository contains a FastAPI-based backend integrated with a complete DevSecOps pipeline using Docker, GitHub Actions, and AWS. It also includes Kubernetes manifests for container orchestration and scaling.
Features
FastAPI backend with modular architecture
Dockerized application with Docker Compose support
CI/CD using GitHub Actions:
Build & push Docker images
Deploy to AWS EC2 via SSH
Code quality & security scanning (Trivy)
AWS Monitoring:
Lists S3 buckets and EC2 instances
Flags resources older than 90 days
Detects newly created resources
☁️ AWS Integration
Uses AWS Access Key & Secret Key via GitHub Secrets
Default region configured via GitHub Variables
Helps monitor infrastructure health and unused resources
🐳 Local Development
git clone https://github.com/your-repo.git
cd your-repo

pip install -r requirements.txt
python main.py

Test:

curl http://localhost:8081
☸️ Kubernetes Deployment
Application is deployed using Kubernetes manifests in k8s/
Uses NodePort service:
Internal app runs on port 8081
Exposed externally via port 30081
🔌 Access
Local (port-forward):
kubectl port-forward service/<service-name> 8081:8081
External:
http://<node-ip>:30081
🔐 Secrets & Configuration
secrets.yml:
Store AWS & Docker credentials
Values must be Base64 encoded (no spaces)
config-map:
Stores non-sensitive configuration
📈 Auto Scaling
Horizontal Pod Autoscaler (HPA) enabled
Automatically scales pods when:
CPU usage ≥ 70%
🚀 Deployment (EC2)

GitHub Actions workflow:

Builds Docker image
Pushes to registry
SSH into EC2
Deploys using Docker Compose

Verify:

curl http://<ec2-ip>:8081
🔍 Security
Trivy scans Docker images for vulnerabilities
Secrets managed securely via GitHub Actions
✅ Summary

This project demonstrates a complete DevSecOps workflow:

Development → CI → Security Scan → Deployment → Monitoring → Scaling






