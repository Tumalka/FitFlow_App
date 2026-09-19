# FitFlow Redesign

[![CI Pipeline](https://github.com/fitflow/fitflow-redesign/actions/workflows/ci.yml/badge.svg)](https://github.com/fitflow/fitflow-redesign/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An intelligent, flow-oriented fitness and workout management platform. FitFlow provides real-time workout guidance, ergonomic flow analysis, and personalized AI recommendations across mobile, web, and desktop.

---

## 5.2 Folder Structure

The repository is organized as a monorepo so that the frontend, backend, AI service, and all supporting documentation stay versioned together:

```text
fitflow-redesign/
|-- README.md
|-- .gitignore
|-- LICENSE
|
|-- frontend/
|   `-- fitflow_app/            # Flutter project (iOS, Android, Web)
|       |-- lib/
|       |-- assets/
|       `-- pubspec.yaml
|
|-- backend/
|   `-- core-api/               # NestJS project
|       |-- src/
|       |-- test/
|       `-- package.json
|
|-- ai-service/
|   `-- app/                    # FastAPI project
|       |-- models/
|       |-- routers/
|       `-- requirements.txt
|
`-- .github/
    `-- workflows/
        `-- ci.yml              # GitHub Actions CI pipeline
```

---

## Repository Components

### 1. Frontend (`frontend/fitflow_app`)
- **Framework**: [Flutter](https://flutter.dev/) (Dart)
- **Target Platforms**: iOS, Android, Web
- **Key Features**: Clean HCI-focused user interface, activity tracking dashboard, workout routine builder, and visual analytics.
- **Getting Started**:
  ```bash
  cd frontend/fitflow_app
  flutter pub get
  flutter run
  ```

### 2. Backend (`backend/core-api`)
- **Framework**: [NestJS](https://nestjs.com/) (Node.js / TypeScript)
- **Role**: Core business logic, user authentication, profile data persistence, workout logs, and API gateway services.
- **Getting Started**:
  ```bash
  cd backend/core-api
  npm install
  npm run start:dev
  ```

### 3. AI Service (`ai-service/app`)
- **Framework**: [FastAPI](https://fastapi.tiangolo.com/) (Python)
- **Role**: Workout recommendation engine, ergonomic posture evaluation, and flow state prediction models.
- **Getting Started**:
  ```bash
  cd ai-service/app
  pip install -r requirements.txt
  uvicorn main:app --reload --port 8000
  ```

### 4. CI/CD (`.github/workflows`)
- Automated GitHub Actions workflow (`ci.yml`) providing linting, build verification, and unit/e2e test execution across all sub-projects on push and pull requests.

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
*(Academic prototype; adjust if the project becomes commercial)*.