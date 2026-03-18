This repository contains a FastAPI application with a complete DevSecOps pipeline using GitHub Actions, Docker, and AWS EC2. It also includes utilities to monitor AWS resources — specifically S3 buckets and EC2 instances — highlighting stale resources and new creations.
Project Structure
- app/ → FastAPI application code
- routers/ → API route definitions
- service/ → Business logic and AWS integrations
- main.py → Entry point for FastAPI
- Dockerfile → Container build instructions
- docker-compose.yml → Service orchestration
- .github/workflows/ → CI/CD pipelines (linting, build, deploy, security scans)
Features
- FastAPI backend with modular routers and services
- Dockerized app with Compose for local and production environments
- GitHub Actions workflows:
- docker-build-push.yml → Build & push Docker images
- deploy-to-server.yml → SSH into EC2 and deploy with Docker Compose
- image-scan.yml & code-quality.yml → Security and lint checks
. AWS Monitoring:
- Fetches all S3 buckets and EC2 instances
- Flags resources older than 90 days
- Displays newly created buckets and EC2 instances
- Secrets & variables managed via GitHub Actions (secrets.*, vars.*)
- Trivy security scanning for images
INHERIT CREDENTIALS
- Inside secrets and variable insert you access key and secret access key in secrets and default region in variables to fetch respective data
  SETUP
Local Development
# Clone repo
git clone https://github.com/your-repo.git
cd your-repo

# Install dependencies
pip install -r requirements.txt

# Run locally
python main.py

# Test with curl
curl http://localhost:8081
AWS Resource Monitoring
The service includes scripts to query AWS and report:
- Stale resources: Buckets and EC2 instances older than 90 days.
- New resources: Recently created buckets and EC2 instances.
This helps track unused infrastructure and spot unexpected creations.
 Verification
After deployment, test the app on EC2:
curl http://<ec2-public-ip>:8081







