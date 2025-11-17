<div align="center">

# 🏋️ ACEest Fitness & Gym Tracker

### Complete CI/CD Pipeline Implementation Guide

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![Docker](https://img.shields.io/badge/Docker-latest-blue.svg)
![Kubernetes](https://img.shields.io/badge/Kubernetes-1.28+-326CE5.svg)
![Jenkins](https://img.shields.io/badge/Jenkins-2.400+-D24939.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**Student Name:** Neha  
**Course:** Introduction to DevOps (CSIZG514/SEZG514)  
**Assignment:** CI/CD Pipeline Implementation  
**Date:** 2024

[Features](#-features) • [Installation](#-quick-start) • [Deployment](#-deployment-strategies) • [Documentation](#-table-of-contents)

</div>

---

## 📋 Table of Contents

- [🎯 Project Overview](#-project-overview)
- [💻 System Requirements](#-system-requirements)
- [🚀 Phase 1: Local Development Setup](#-phase-1-local-development-setup)
- [🐳 Phase 2: Docker Configuration](#-phase-2-docker-configuration)
- [📦 Phase 3: Git Version Control](#-phase-3-git-version-control)
- [☸️ Phase 4: Kubernetes Deployment](#️-phase-4-kubernetes-deployment)
- [🎨 Phase 5: Deployment Strategies](#-phase-5-deployment-strategies)
- [🔄 Phase 6: Jenkins CI/CD Pipeline](#-phase-6-jenkins-cicd-pipeline)
- [📊 Phase 7: SonarQube Code Quality](#-phase-7-sonarqube-code-quality)
- [✅ Phase 8: Testing & Verification](#-phase-8-testing--verification)
- [🔧 Troubleshooting Guide](#-troubleshooting-guide)
- [📝 Submission Checklist](#-submission-checklist)

---

## 🎯 Project Overview

### ✨ Features

- 🏃 **Workout Logging** - Track exercises and duration
- 👤 **User Management** - Store user information and calculate BMI
- 📊 **Workout Summary** - View total workouts and time spent
- 🔌 **RESTful API** - Complete API for all operations
- 📱 **Responsive Design** - Modern UI with smooth animations

### 🏗️ Architecture Diagram

```mermaid
graph TD
    A[GitHub Repository] --> B[Jenkins Pipeline]
    B --> C[Checkout Code]
    B --> D[Run Unit Tests]
    B --> E[SonarQube Analysis]
    B --> F[Build Docker Image]
    B --> G[Push to Docker Hub]
    B --> H[Deploy to Kubernetes]
    H --> I[Blue-Green]
    H --> J[Canary]
    H --> K[Rolling Update]
    H --> L[Shadow]
    H --> M[A/B Testing]
```

### 🛠️ Technology Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| 🐍 Application | Flask (Python) | 3.9+ |
| 📂 Version Control | Git, GitHub | Latest |
| 🔨 Build Automation | Jenkins | 2.400+ |
| ✅ Testing | Pytest | 7.4.3 |
| 📈 Code Quality | SonarQube | Latest |
| 🐳 Containerization | Docker | Latest |
| 📦 Container Registry | Docker Hub | - |
| ☸️ Orchestration | Kubernetes | 1.28+ |
| 🔄 CI/CD | Jenkins Pipeline | - |

---

## 💻 System Requirements

### 📦 Software Requirements

| Software | Version | Required |
|----------|---------|----------|
| 🪟 Windows | 10/11 (64-bit) | ✅ Yes |
| 🐍 Python | 3.9+ | ✅ Yes |
| 🐳 Docker Desktop | Latest | ✅ Yes |
| 📂 Git | 2.40+ | ✅ Yes |
| ☸️ Minikube | Latest | ✅ Yes |
| 🔧 kubectl | Latest | ✅ Yes |
| 🔨 Jenkins | 2.400+ | ✅ Yes |
| 💻 VS Code | Latest | ⚪ Optional |

### 🖥️ Hardware Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| 💾 RAM | 8GB | 16GB |
| 💿 Storage | 20GB free | 50GB free |
| ⚙️ Processor | Intel i5 | Intel i7 or equivalent |

---

## 🚀 Phase 1: Local Development Setup

### 📁 Step 1.1: Create Project Structure

```bash
# Open Command Prompt
cd Desktop

# Create main project folder
mkdir ACEest_Fitness
cd ACEest_Fitness

# Create subdirectories
mkdir templates static tests kubernetes
mkdir kubernetes\blue-green kubernetes\canary kubernetes\rolling kubernetes\shadow kubernetes\ab-testing
```

### 📦 Step 1.2: Install Python Dependencies

**Create `requirements.txt`:**

```text
Flask==3.0.0
pytest==7.4.3
pytest-flask==1.3.0
Werkzeug==3.0.1
gunicorn==21.2.0
requests==2.31.0
```

**Install dependencies:**

```bash
pip install -r requirements.txt
```

### ⚙️ Step 1.3: Create Flask Application

**File:** `app.py`

**Key components:**
- ✅ Flask web server setup
- 🔐 Session management
- 🔌 RESTful API endpoints
- ⚠️ Error handling
- ❤️ Health check endpoint

**Main Routes:**
- `GET /` - 🏠 Home page
- `POST /api/workouts` - ➕ Add workout
- `GET /api/workouts` - 📋 Get all workouts
- `GET /api/workouts/summary` - 📊 Get summary
- `POST /api/user` - 💾 Save user info
- `GET /api/user` - 👤 Get user info
- `GET /health` - ❤️ Health check
![API calls](images/APIs.png)

### 🎨 Step 1.4: Create Frontend

**File:** `templates/index.html`
- 📱 Responsive design with tabs
- 🏋️ Workout logging interface
- 📊 Summary view
- 👤 User information form

**File:** `static/style.css`
- 🎨 Modern gradient design
- 📐 Responsive layout
- ✨ Smooth animations
- 💼 Professional styling

### 🧪 Step 1.5: Test Locally

```bash
# Run the application
python app.py

# Access in browser
# 🌐 http://localhost:5000
```

**Test functionality:**
1. ✅ Add a workout
![Log Workouts](images/Log_Workouts.png)
2. ✅ View summary
![View Summary](images/View_Summary.png)
3. ✅ Save user info
![User Info](images/User_Info.png)
4. ✅ Check calculations

**Expected Output:**

```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

---

## 🐳 Phase 2: Docker Configuration

### 📄 Step 2.1: Create Dockerfile

**File:** `Dockerfile`

**Key features:**
- 🐍 Python 3.9 slim base image
- ⚡ Multi-stage optimization
- 🔐 Non-root user for security
- ❤️ Health check included
- 🚀 Gunicorn for production

### 🚫 Step 2.2: Create .dockerignore

**File:** `.dockerignore`

**Excludes:**
- 🗑️ Python cache files
- 📦 Virtual environments
- 🧪 Test files
- 📂 Git files
- 💻 IDE configurations

### 🏗️ Step 2.3: Build Docker Image

```bash
# Build image (replace neha with your Docker Hub username)
docker build -t nehaavalur/aceest-fitness:v1.0 .

# Tag as latest
docker tag nehaavalur/aceest-fitness:v1.0 nehaavalur/aceest-fitness:latest

# Verify image
docker images | grep aceest-fitness
```

**Expected Output:**

![Docker Images](images/Docker_Images.png)

### 🚀 Step 2.4: Test Docker Container

```bash
# Run container
docker run -d -p 5000:5000 --name aceest-app nehaavalur/aceest-fitness:v1.0

# Check if running
docker ps

# Check logs
docker logs aceest-app

# Test in browser
# 🌐 http://localhost:5000

# Stop and remove
docker stop aceest-app
docker rm aceest-app
```
![Running Docker Image](images/Running_Docker_Image.png)

![Docker Logs](images/Docker_Logs.png)

### 📤 Step 2.5: Push to Docker Hub

```bash
# Login to Docker Hub
docker login
# Enter username and password

# Push images
docker push nehaavalur/aceest-fitness:v1.0
docker push nehaavalur/aceest-fitness:latest

# Verify on Docker Hub
# 🌐 https://hub.docker.com/r/neha/aceest-fitness
```
![Docker Hub Verification](images/Docker_Hub_Verification.png)

---

## 📦 Phase 3: Git Version Control

### ⚙️ Step 3.1: Install and Configure Git

```bash
# Install Git from: https://git-scm.com/download/win

# Configure Git
git config --global user.name "Neha"
git config --global user.email "your.email@example.com"

# Verify
git config --list
```

### 🆕 Step 3.2: Create GitHub Repository

1. 🌐 Go to https://github.com
2. ➕ Click "+" → "New repository"
3. 📝 Name: `aceest-fitness`
4. 📄 Description: "DevOps CI/CD Pipeline Assignment"
5. 🌍 Public repository
6. ❌ Don't initialize with README
7. ✅ Create repository

### 🎬 Step 3.3: Initialize Local Repository

```bash
# In project folder
cd ACEest_Fitness

# Initialize Git
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit: ACEest Fitness v1.0 - Complete CI/CD pipeline"

# Rename branch to main
git branch -M main

# Add remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/aceest-fitness.git

# Push to GitHub
git push -u origin main
```

### 🏷️ Step 3.4: Create Version Tags

```bash
# Create version tag
git tag -a v1.0 -m "Version 1.0: Initial release with full CI/CD"

# Push tag
git push origin v1.0

# Verify on GitHub
# 🌐 https://github.com/YOUR_USERNAME/aceest-fitness
```

### 🔄 Step 3.5: Git Workflow for Updates

```bash
# Make changes to files

# Check status
git status

# Add changes
git add .

# Commit with message
git commit -m "Description of changes"

# Push to GitHub
git push origin master

# Create new version tag
git tag -a v1.1 -m "Version 1.1: Description"
git push origin v1.1
```

---

## ☸️ Phase 4: Kubernetes Deployment

### 📥 Step 4.1: Install Minikube

```bash
# Download from: https://minikube.sigs.k8s.io/docs/start/

# Start Minikube
minikube start

# Verify installation
kubectl version
kubectl get nodes
```

**Expected Output:**

![Minikube](images/Minikube.png)

### 🏷️ Step 4.2: Create Namespace

**File:** `kubernetes/namespace.yaml`

```bash
# Apply namespace
kubectl apply -f kubernetes/namespace.yaml

# Verify
kubectl get namespaces
```
![Namespaces](images/Namespaces.png)

### 🔐 Step 4.3: Create Secrets

**File:** `kubernetes/secrets.yaml`

**Generate base64 secret:**

```bash
# macOS/Linux
echo -n "your-secret-key-here" | base64

# Windows PowerShell
$text = "your-secret-key-here"
$bytes = [System.Text.Encoding]::UTF8.GetBytes($text)
[Convert]::ToBase64String($bytes)
```

**Apply secrets:**

```bash
kubectl apply -f kubernetes/secrets.yaml
```

### 🚀 Step 4.4: Deploy Application

```bash
# Deploy application
kubectl apply -f kubernetes/deployment.yaml

# Create service
kubectl apply -f kubernetes/service.yaml

# Check deployment status
kubectl get all -n aceest-fitness

# Wait for pods to be ready
kubectl wait --for=condition=ready pod -l app=aceest-fitness -n aceest-fitness --timeout=300s
```
![Deployment status](images/Deployment_status.png)

### 🌐 Step 4.5: Access Application

```bash
# Get service URL
minikube service aceest-fitness-service -n aceest-fitness

# Or use port forwarding
kubectl port-forward -n aceest-fitness svc/aceest-fitness-service 8080:80

# Access in browser
# 🌐 http://localhost:8080
```
![Minikube service](images/Minikube_Service.png)
![Minikube Application](images/Minikube_Application.png)

### 📊 Step 4.6: Monitor Deployment

```bash
# Get pods
kubectl get pods -n aceest-fitness

# Get pod details
kubectl describe pod aceest-fitness-deployment-559765f44b-cqqst -n aceest-fitness

# View logs
kubectl logs aceest-fitness-deployment-559765f44b-cqqst -n aceest-fitness

# Watch pods in real-time
kubectl get pods -n aceest-fitness -w
```
![Pods](images/Pods.png)

![Pod Details 1](images/Pod_Details_1.png)
![Pod Details 2](images/Pod_Details_2.png)

![Pod Logs](images/Pod_Logs.png)

---

## 🎨 Phase 5: Deployment Strategies

### 🔵🟢 Strategy 1: Blue-Green Deployment

**Concept:** Two identical environments (blue and green). Switch traffic instantly between versions.

**Files:**
- `kubernetes/blue-green/blue-deployment.yaml`
- `kubernetes/blue-green/green-deployment.yaml`
- `kubernetes/blue-green/service.yaml`

**Implementation:**

```bash
# Deploy blue version (v1.0)
kubectl apply -f kubernetes/blue-green/blue-deployment.yaml

# Deploy green version (v1.1)
kubectl apply -f kubernetes/blue-green/green-deployment.yaml

# Deploy service (initially points to blue)
kubectl apply -f kubernetes/blue-green/service.yaml

# Access blue version
minikube service aceest-fitness-bluegreen -n aceest-fitness

# Switch to green
kubectl patch service aceest-fitness-bluegreen -n aceest-fitness -p '{"spec":{"selector":{"version":"green"}}}'

# Rollback to blue if needed
kubectl patch service aceest-fitness-bluegreen -n aceest-fitness -p '{"spec":{"selector":{"version":"blue"}}}'

# Verify active version
kubectl describe service aceest-fitness-bluegreen -n aceest-fitness
```

![Blue Deployment](images/Blue_Deployment.png)

![Changed Active Version to Green](images/Green_Deployment_Active.png)

![Rollback to Blue](images/Rollback_To_Blue.png)

**Benefits:**
- ✅ Instant rollback
- ✅ Zero downtime
- ✅ Easy testing before switch

---

### 🐤 Strategy 2: Canary Release

**Concept:** Gradually shift traffic from stable to new version. Start with 10%, increase if successful.

**File:** `kubernetes/canary/canary-deployment.yaml`

**Implementation:**


```bash
# Deploy stable version (9 replicas = 90% traffic)
kubectl apply -f kubernetes/canary/canary-deployment.yaml

# Initially: 9 stable + 1 canary = 10% canary traffic

# Monitor canary performance
kubectl logs -l track=canary -n aceest-fitness

# ✅ If successful, increase canary to 30%
kubectl scale deployment aceest-fitness-canary --replicas=3 -n aceest-fitness
kubectl scale deployment aceest-fitness-stable --replicas=7 -n aceest-fitness

# ✅ Continue increasing to 50%
kubectl scale deployment aceest-fitness-canary --replicas=5 -n aceest-fitness
kubectl scale deployment aceest-fitness-stable --replicas=5 -n aceest-fitness

# ✅ Full rollout (100%)
kubectl scale deployment aceest-fitness-canary --replicas=10 -n aceest-fitness
kubectl scale deployment aceest-fitness-stable --replicas=0 -n aceest-fitness

# ❌ Rollback if issues
kubectl scale deployment aceest-fitness-stable --replicas=10 -n aceest-fitness
kubectl scale deployment aceest-fitness-canary --replicas=0 -n aceest-fitness
```
![Track canary deployments](images/Track_Canary.png)

**Benefits:**
- ✅ Controlled risk
- ✅ Real-world testing
- ✅ Gradual migration

---

### 🔄 Strategy 3: Rolling Update

**Concept:** Kubernetes native strategy. Gradually replaces old pods with new ones.

**File:** `kubernetes/rolling/rolling-deployment.yaml`

**Implementation:**

```bash
# Deploy initial version
kubectl apply -f kubernetes/rolling/rolling-deployment.yaml

# Update to new version
kubectl set image deployment/aceest-fitness-rolling aceest-fitness=neha/aceest-fitness:v1.1 -n aceest-fitness

# Watch the rollout
kubectl rollout status deployment/aceest-fitness-rolling -n aceest-fitness

# ⏸️ Pause rollout (if needed)
kubectl rollout pause deployment/aceest-fitness-rolling -n aceest-fitness

# ▶️ Resume rollout
kubectl rollout resume deployment/aceest-fitness-rolling -n aceest-fitness

# 📜 Check history
kubectl rollout history deployment/aceest-fitness-rolling -n aceest-fitness

# ↩️ Rollback to previous version
kubectl rollout undo deployment/aceest-fitness-rolling -n aceest-fitness

# ↩️ Rollback to specific revision
kubectl rollout undo deployment/aceest-fitness-rolling --to-revision=2 -n aceest-fitness
```
![Rolling out deployments](images/Rolling_Out_Deployments.png)

![Rolling Deployment Created](images/Rolling_Deployment_Created.png)

![Rolling to revision 1](images/Rolling_Revisions.png)

**Configuration:**

```yaml
strategy:
  type: RollingUpdate
  rollingUpdate:
    maxSurge: 1        # Max new pods created at once
    maxUnavailable: 1  # Max pods unavailable during update
```

**Benefits:**
- ✅ Zero downtime
- ✅ Automatic rollback on failure
- ✅ Built-in Kubernetes feature

---

### 👥 Strategy 4: Shadow Deployment

**Concept:** New version receives copy of production traffic but doesn't respond to users. Used for testing under real load.

**File:** `kubernetes/shadow/shadow-deployment.yaml`

**Implementation:**

```bash
# Deploy production and shadow
kubectl apply -f kubernetes/shadow/shadow-deployment.yaml

# Production serves real users
# Shadow processes same requests but doesn't respond

# Monitor shadow logs
kubectl logs -l environment=shadow -n aceest-fitness -f

# Compare metrics
kubectl top pods -n aceest-fitness -l environment=production
kubectl top pods -n aceest-fitness -l environment=shadow

# ✅ If shadow performs well, promote to production
kubectl set image deployment/aceest-fitness-production aceest-fitness=neha/aceest-fitness:v1.1 -n aceest-fitness
```
![Shadow deployment](images/Shadow_Deployment.png)

![Metrics](images/Metrics.png)

> **Note:** Full shadow deployment requires service mesh like Istio for traffic mirroring.

**Benefits:**
- ✅ Test in production without user impact
- ✅ Identify issues before release
- ✅ Performance comparison

---

### 🧪 Strategy 5: A/B Testing

**Concept:** Run two versions simultaneously. Split traffic based on criteria to compare performance.

**File:** `kubernetes/ab-testing/ab-testing.yaml`

**Implementation:**

```bash
# Deploy both versions (50/50 split)
kubectl apply -f kubernetes/ab-testing/ab-testing.yaml
# 5 replicas version A + 5 replicas version B

# Access service
minikube service aceest-fitness-ab-service -n aceest-fitness

# Traffic splits randomly between A and B
# SessionAffinity ensures same user gets same version

# Adjust traffic split (70% A, 30% B)
kubectl scale deployment aceest-fitness-version-a --replicas=7 -n aceest-fitness
kubectl scale deployment aceest-fitness-version-b --replicas=3 -n aceest-fitness

# Monitor metrics for both versions
kubectl logs -l version=a -n aceest-fitness
kubectl logs -l version=b -n aceest-fitness

# Promote winning version (if B wins)
kubectl scale deployment aceest-fitness-version-b --replicas=10 -n aceest-fitness
kubectl scale deployment aceest-fitness-version-a --replicas=0 -n aceest-fitness
```
![AB Deployment](images/AB_Deployment.png)
**Benefits:**
- ✅ Data-driven decisions
- ✅ Compare user engagement
- ✅ Feature flag testing

---

### 📊 Deployment Strategy Comparison

| Strategy | Use Case | Downtime | Rollback Speed | Complexity | Risk Level |
|----------|----------|----------|----------------|------------|------------|
| 🔵🟢 Blue-Green | Major releases | ✅ Zero | ⚡ Instant | 🟡 Medium | 🟢 Low |
| 🐤 Canary | Gradual rollout | ✅ Zero | ⚡ Fast | 🟡 Medium | 🟢 Low |
| 🔄 Rolling | Standard updates | ✅ Zero | 🟡 Medium | 🟢 Low | 🟢 Low |
| 👥 Shadow | Testing in prod | ✅ Zero | ➖ N/A | 🔴 High | 🟢 Very Low |
| 🧪 A/B Testing | Feature comparison | ✅ Zero | 🟡 Medium | 🔴 High | 🟡 Medium |

---

## 🔄 Phase 6: Jenkins CI/CD Pipeline

### 📥 Step 6.1: Install Jenkins

**Option 1: Docker (Recommended) 🐳**

```bash
# Run Jenkins in Docker
docker run -d -p 8080:8080 -p 50000:50000 --name jenkins \
  -v jenkins_home:/var/jenkins_home \
  jenkins/jenkins:lts

# Get initial admin password
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```
![Jenkins](image.png)

**Option 2: Windows Installer 🪟**

1. Download from: https://www.jenkins.io/download/
2. Run installer
3. Access: 🌐 http://localhost:8080

### 🔓 Step 6.2: Initial Jenkins Setup

1. **Unlock Jenkins:**
   - 🔑 Copy initial admin password
   - 📋 Paste in unlock screen

2. **Install Plugins:**
   - ✅ Select "Install suggested plugins"
   - ⏳ Wait for installation

3. **Create Admin User:**
   - 👤 Username: neha
   - 🔐 Password: 1ea46836215f44deb71aea70457ece94
   - 📝 Full name: Neha
   - 📧 Email: your.email@example.com

4. **Jenkins URL:**
   - ✅ Keep default: http://localhost:8080/

### 🔌 Step 6.3: Install Required Plugins

Navigate to: **Manage Jenkins → Plugins → Available plugins**

**Install:**
- ✅ Docker Pipeline
- ✅ Docker Commons
- ✅ Kubernetes
- ✅ Kubernetes CLI
- ✅ SonarQube Scanner
- ✅ GitHub Integration
- ✅ Pipeline
- ✅ Pipeline: Stage View
- ✅ Email Extension Plugin

**🔄 Restart Jenkins after installation**

### 🐳 Step 6.4: Configure Docker in Jenkins

1. **Manage Jenkins → System**
2. **Add Docker:**
   - 🐧 Docker URL: `unix:///var/run/docker.sock` (Linux)
   - 🪟 Or: `npipe:////./pipe/docker_engine` (Windows)
   - ✅ Test connection

### 🔑 Step 6.5: Add Credentials

**Navigate to:** Manage Jenkins → Credentials → System → Global credentials

**Add Docker Hub Credentials:**
- 📦 Kind: Username with password
- 👤 Username: [your Docker Hub username]
- 🔐 Password: [your Docker Hub password]
- 🆔 ID: `dockerhub-credentials`
- 📝 Description: Docker Hub Login

**Add Kubernetes Config:**

```bash
# Get kubeconfig content
kubectl config view --raw > kubeconfig.yaml
```

- 📦 Kind: Secret file
- 📁 File: Upload `kubeconfig.yaml`
- 🆔 ID: `kubeconfig-credentials`
- 📝 Description: Kubernetes Config

**Add GitHub Token (optional):**
- 📦 Kind: Secret text
- 🔑 Secret: [GitHub Personal Access Token]
- 🆔 ID: `github-token`
- 📝 Description: GitHub Access

### 🚀 Step 6.6: Create Jenkins Pipeline

1. ➕ **New Item**
2. 📝 **Enter name:** ACEest-Fitness-Pipeline
3. 🔧 **Select:** Pipeline
4. ✅ **Click OK**

**Configure Pipeline:**

**General:**
- 📄 Description: "CI/CD pipeline for ACEest Fitness application"
- 🔗 GitHub project: https://github.com/YOUR_USERNAME/aceest-fitness

**Build Triggers:**
- ☑️ GitHub hook trigger for GITScm polling
- ☑️ Poll SCM: `H/5 * * * *` (every 5 minutes)

**Pipeline:**
- 📝 Definition: Pipeline script from SCM
- 📂 SCM: Git
- 🔗 Repository URL: https://github.com/YOUR_USERNAME/aceest-fitness.git
- 🔑 Credentials: (add if private repo)
- 🌿 Branch Specifier: `*/main`
- 📄 Script Path: `Jenkinsfile`

**💾 Save**

### 🪝 Step 6.7: Configure GitHub Webhook

1. 🌐 **Go to GitHub repository**
2. ⚙️ **Settings → Webhooks → Add webhook**
3. 🔗 **Payload URL:** `http://YOUR_JENKINS_URL:8080/github-webhook/`
4. 📦 **Content type:** `application/json`
5. 🎯 **Select:** Just the push event
6. ✅ **Active:** ☑
7. ➕ **Add webhook**

### ▶️ Step 6.8: Run Pipeline

1. 🚀 **Click "Build Now"**
2. 👀 **Watch Console Output**
3. 📊 **Monitor each stage:**
   - ✅ Checkout
   - ✅ Environment Setup
   - ✅ Unit Tests
   - ✅ Code Quality Analysis
   - ✅ Quality Gate
   - ✅ Build Docker Image
   - ✅ Push to Docker Hub
   - ✅ Deploy to Kubernetes
   - ✅ Verify Deployment

### 📋 Step 6.9: Pipeline Stages Explained

| Stage | Description | Duration |
|-------|-------------|----------|
| 🔄 **Checkout** | Clones code from GitHub, verifies branch | ~10s |
| ⚙️ **Environment Setup** | Installs Python dependencies | ~30s |
| 🧪 **Unit Tests** | Runs pytest tests, generates reports | ~20s |
| 📊 **Code Quality** | SonarQube scans code for issues | ~40s |
| ✅ **Quality Gate** | Checks SonarQube thresholds | ~5s |
| 🐳 **Build Docker** | Builds and tags Docker image | ~60s |
| 📤 **Push to Hub** | Pushes image to Docker Hub | ~30s |
| ☸️ **Deploy K8s** | Updates Kubernetes deployment | ~45s |
| ✔️ **Verify** | Checks pod status and service | ~15s |

---

## 📊 Phase 7: SonarQube Code Quality

### 📥 Step 7.1: Install SonarQube

**Using Docker: 🐳**

```bash
# Run SonarQube
docker run -d --name sonarqube -p 9000:9000 sonarqube:latest

# Wait 2-3 minutes for startup

# Access SonarQube
# 🌐 http://localhost:9000
```

**Default Credentials:**
- 👤 Username: `admin`
- 🔐 Password: `admin`
- ⚠️ (Change password on first login)

### 🆕 Step 7.2: Create SonarQube Project

1. ➕ **Click "Create Project"**
2. 🔑 **Project key:** `aceest-fitness`
3. 📝 **Display name:** ACEest Fitness & Gym Tracker
4. ✅ **Click "Set Up"**

### 🔑 Step 7.3: Generate Token

1. 🎯 **Choose "With Jenkins"**
2. 🔑 **Generate token**
3. 📋 **Copy token** (you'll need this)
4. 📝 **Token name:** `jenkins-aceest`

### ⚙️ Step 7.4: Configure SonarQube in Jenkins

**Manage Jenkins → System → SonarQube servers:**

- 📝 Name: `SonarQube`
- 🔗 Server URL: `http://localhost:9000`
- 🔑 Server authentication token:
  - ➕ Add credential → Secret text
  - 🔒 Secret: [paste token from Step 7.3]
  - 🆔 ID: `sonarqube-token`
  - 📝 Description: SonarQube Token

### 🔧 Step 7.5: Install SonarQube Scanner

**Manage Jenkins → Global Tool Configuration:**

- 🔍 **SonarQube Scanner**
- ➕ Click "Add SonarQube Scanner"
- 📝 Name: `SonarQubeScanner`
- ☑️ Install automatically
- 📦 Version: Latest

### 📄 Step 7.6: Create sonar-project.properties

**File:** `sonar-project.properties`

```properties
sonar.projectKey=aceest-fitness
sonar.projectName=ACEest Fitness & Gym Tracker
sonar.projectVersion=1.0
sonar.sources=.
sonar.exclusions=tests/**,venv/**,static/**,templates/**
sonar.python.coverage.reportPaths=coverage.xml
sonar.python.version=3.9
```

### 🚀 Step 7.7: Run Analysis

**Manual Run:**

```bash
# Install sonar-scanner
# Download from: https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/

# Run analysis
sonar-scanner
```
![SonarQube](images/SonarQube.png)
![SonarQube Analysis](images/SonarQube_Analysis.png)

**Via Jenkins:**
- 🔄 Pipeline automatically runs analysis
- 📊 View results in SonarQube dashboard

### 📈 Step 7.8: Understanding SonarQube Metrics

**Quality Gate Criteria:**

| Metric | Threshold | Status |
|--------|-----------|--------|
| 📊 Code Coverage | > 80% | ✅ Pass |
| 📋 Duplicated Lines | < 3% | ✅ Pass |
| 🔧 Maintainability | A | ✅ Pass |
| 🛡️ Reliability | A | ✅ Pass |
| 🔒 Security | A | ✅ Pass |

**Metrics Explained:**
- 🐛 **Bugs:** Potential runtime errors
- 🔓 **Vulnerabilities:** Security issues
- 👃 **Code Smells:** Maintainability issues
- 📊 **Coverage:** Test coverage percentage
- 📋 **Duplications:** Duplicated code blocks
- 🧩 **Complexity:** Cyclomatic complexity

### 🔧 Step 7.9: Fix Issues

**Priority Levels:**

1. 🔴 **Blocker** - Must fix immediately
2. 🟠 **Critical** - Fix ASAP
3. 🟡 **Major** - Fix soon
4. 🔵 **Minor** - Fix when possible
5. ⚪ **Info** - Nice to have

**Workflow:**
1. 👀 View issues in SonarQube
2. 📝 Fix in code
3. 💾 Commit and push
4. 🔄 Jenkins re-runs analysis
5. ✅ Verify fixes

![Jenkins Pipeline](images/Jenkins_Pipeline.png)
---

## ✅ Phase 8: Testing & Verification

### 🧪 Step 8.1: Unit Testing with Pytest

**Run all tests:**

```bash
pytest
```

**Run with verbose output:**

```bash
pytest -v
```
![Pytest](images/Pytest.png)

*Run with coverage:*
bash
pytest --cov=app --cov-report=html


*Test results location:*
- HTML Report: htmlcov/index.html
- XML Report: coverage.xml

![Files Coverage](images/Files_Coverage.png)
![Functions Coverage](images/Functions_Coverage.png)
![Classes Coverage](images/Classes_Coverage.png)

### Step 8.2: Test Categories

*1. Route Tests (6 tests)*
- Home page loads
- Version displayed correctly
- Health endpoint works

*2. Workout API Tests (8 tests)*
- Add workout successfully
- Get workouts
- Handle missing fields
- Validate duration
- Summary calculations

*3. User API Tests (6 tests)*
- Save user info
- Get user info
- BMI calculations
- Input validation

*4. Integration Tests (4 tests)*
- Complete workflows
- Data persistence
- Multiple operations

*Total: 24 tests*

### Step 8.3: Manual Testing Checklist

*Application Features:*
- [ ] Home page loads
- [ ] Add workout form works
- [ ] Duration validation works
- [ ] Workout list displays
- [ ] Summary shows correct totals
- [ ] User info saves
- [ ] BMI calculates correctly
- [ ] Session persists

*API Endpoints:*
bash
# Health check
curl http://localhost:5000/health

# Add workout
curl -X POST http://localhost:5000/api/workouts \
  -H "Content-Type: application/json" \
  -d '{"workout":"Push-ups","duration":30}'

# Get workouts
curl http://localhost:5000/api/workouts

# Save user
curl -X POST http://localhost:5000/api/user \
  -H "Content-Type: application/json" \
  -d '{"name":"Neha","age":25,"weight":60,"height":165}'


### Step 8.4: Docker Testing

bash
# Build and run
docker build -t neha/aceest-fitness:test .
docker run -d -p 5000:5000 --name test-app neha/aceest-fitness:test

# Test container
curl http://localhost:5000/health

# Check logs
docker logs test-app

# Stop and remove
docker stop test-app
docker rm test-app


### Step 8.5: Kubernetes Testing

bash
# Deploy test version
kubectl apply -f kubernetes/deployment.yaml

# Check status
kubectl get pods -n aceest-fitness

# Test service
kubectl port-forward -n aceest-fitness svc/aceest-fitness-service 8080:80
curl http://localhost:8080/health

# Check logs
kubectl logs -n aceest-fitness -l app=aceest-fitness

# Clean up
kubectl delete -f kubernetes/deployment.yaml


### Step 8.6: Deployment Strategy Testing

*Test each strategy:*

bash
# 1. Blue-Green
kubectl apply -f kubernetes/blue-green/
# Verify traffic switches correctly

# 2. Canary
kubectl apply -f kubernetes/canary/
# Verify traffic distribution

# 3. Rolling
kubectl apply -f kubernetes/rolling/
# Verify gradual update

# 4. Shadow
kubectl apply -f kubernetes/shadow/
# Verify shadow logs

# 5. A/B Testing
kubectl apply -f kubernetes/ab-testing/
# Verify traffic split


REPOSITORY LINKS:
==================

1. GitHub Repository:
   URL: https://github.com/neha200/2024tm93170_DevOps_Assignment2
   Branch: main
   Latest Commit: [commit hash]

2. Docker Hub Repository:
   URL: https://hub.docker.com/repository/docker/nehaavalur/aceest-fitness/general
   Images:
   - nehaavalur/aceest-fitness:v1.0
   - nehaavalur/aceest-fitness:v1.1
   - nehaavalur/aceest-fitness:latest

3. Jenkins:
   Local URL: http://localhost:8080/job/ACEest-Fitness-Pipeline/
   Latest Build: #35
   Status: SUCCESS

4. SonarQube:
   Local URL: http://localhost:9000/dashboard?id=aceest-fitness
   Quality Gate: PASSED
   Coverage: ![Coverage](images/SonarQube_Coverage.png)

5. Kubernetes Endpoints:
   Namespace: aceest-fitness
   
   Main Application:
   - Service: aceest-fitness-service
   - URL: http://127.0.0.1:51210
   
   Blue-Green Deployment:
   - NodePort: 30081
   - URL: http://localhost:30081
   
   Canary Deployment:
   - NodePort: 30082
   - URL: http://localhost:30082
   
   Rolling Update:
   - NodePort: 30083
   - URL: http://localhost:30083
   
   Shadow Deployment:
   - NodePort: 30084
   - URL: http://localhost:30084
   
   A/B Testing:
   - NodePort: 30085
   - URL: http://localhost:30085

DEPLOYMENT STRATEGIES IMPLEMENTED:
===================================

1. Blue-Green Deployment
   Status: ✓ Implemented and Tested
   Description: Zero-downtime deployment with instant rollback

2. Canary Release
   Status: ✓ Implemented and Tested
   Description: Gradual rollout with 10% initial traffic

3. Rolling Update
   Status: ✓ Implemented and Tested
   Description: Kubernetes native rolling update strategy

4. Shadow Deployment
   Status: ✓ Implemented and Tested
   Description: Testing in production without user impact

5. A/B Testing
   Status: ✓ Implemented and Tested
   Description: 50/50 traffic split for feature comparison


APPLICATION VERSIONS:
====================

v1.0: Initial release with core features
v1.1: Enhanced UI and additional features
v1.2: Advanced features (if implemented)
latest: Points to v1.0
