# ACEest Fitness & Gym Tracker

A comprehensive fitness tracking web application with full CI/CD pipeline implementation.

## Features

- **Workout Logging**: Track exercises and duration
- **User Management**: Store user information and calculate BMI
- **Workout Summary**: View total workouts and time spent
- **RESTful API**: Complete API for all operations
- **Responsive Design**: Modern UI with smooth animations

## Architecture

- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Backend**: Flask (Python)
- **Testing**: Pytest
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **CI/CD**: Jenkins
- **Code Quality**: SonarQube
- **Container Registry**: Docker Hub

## Prerequisites

- Python 3.9+
- Docker
- Kubernetes (Minikube or Cloud)
- Jenkins
- Git

##  Local Development Setup

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Visit: `http://localhost:5000`

### Run Tests

```bash
pytest
```

Or with coverage:

```bash
pytest --cov=app --cov-report=html
```

##  Docker

### Build Image

```bash
docker build -t aceest-fitness:v1.0 .
```

### Run Container

```bash
docker run -d -p 5000:5000 aceest-fitness:v1.0
```

### Push to Docker Hub

```bash
docker tag aceest-fitness:v1.0 nehaavalur/aceest-fitness:v1.0
docker push nehaavalur/aceest-fitness:v1.0
```

##  Kubernetes Deployment

### Deploy to Kubernetes

```bash
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
```

### Check Status

```bash
kubectl get pods
kubectl get services
```

##  CI/CD Pipeline

The Jenkins pipeline automatically:

1. Pulls code from GitHub
2. Runs Pytest tests
3. Performs SonarQube code analysis
4. Builds Docker image
5. Pushes to Docker Hub
6. Deploys to Kubernetes

## Deployment Strategies Implemented

1. **Blue-Green Deployment**: Zero-downtime deployments
2. **Canary Release**: Gradual rollout to subset of users
3. **Rolling Update**: Incremental pod replacement
4. **Shadow Deployment**: Test in production without impact
5. **A/B Testing**: Compare different versions

## API Endpoints

### Workouts
- `GET /api/workouts` - Get all workouts
- `POST /api/workouts` - Add new workout
- `GET /api/workouts/summary` - Get workout summary

### User
- `GET /api/user` - Get user info
- `POST /api/user` - Save user info

### Health
- `GET /health` - Health check endpoint

## Project Structure

```
ACEest_Fitness/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── Dockerfile             # Docker configuration
├── Jenkinsfile            # Jenkins pipeline
├── pytest.ini             # Pytest configuration
├── templates/             # HTML templates
├── static/                # CSS and static files
├── tests/                 # Test cases
└── kubernetes/            # Kubernetes manifests
```

## Security

- Non-root Docker user
- Security headers enabled
- Input validation on all endpoints
- Secret key management via environment variables

##  Version History

- **v1.0** - Initial release with basic features
- **v1.1** - Enhanced UI and workout categories
- **v1.2** - Added charts and progress tracking
- **v1.3** - BMI/BMR calculations and PDF reports

## Contributors

- nehaavalur A - DevOps Engineer

