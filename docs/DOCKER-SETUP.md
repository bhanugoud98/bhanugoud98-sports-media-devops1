# 🐳 Docker Setup Documentation — Sports Media DevOps

## 🎯 Objective
Containerize the microservices (`product`, `user`, and `order`) for consistent local development and testing.

---

## 🧩 Folder Structure
sports-media-devops/
├── product-service/
│ ├── app.py
│ ├── requirements.txt
│ └── Dockerfile
├── user-service/
│ ├── app.py
│ ├── requirements.txt
│ └── Dockerfile
├── order-service/
│ ├── app.py
│ ├── requirements.txt
│ └── Dockerfile
├── docker-compose.yml
└── docs/
└── DOCKER-SETUP.md

yaml
Copy code

---

## ⚙️ Dockerfile (Common Template)
Each microservice uses the same base configuration:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
Change EXPOSE port per service:

product-service → 5000

user-service → 5001

order-service → 5002

🧱 docker-compose.yml
Located in the root folder:

yaml
Copy code
version: "3"
services:
  product-service:
    build: ./product-service
    ports:
      - "5000:5000"
    container_name: product-service

  user-service:
    build: ./user-service
    ports:
      - "5001:5001"
    container_name: user-service

  order-service:
    build: ./order-service
    ports:
      - "5002:5002"
    container_name: order-service
🚀 Build & Run Containers
bash
Copy code
docker compose up --build -d
Check running containers:

bash
Copy code
docker ps
🔍 Verify Health of Services
bash
Copy code
curl http://localhost:5000/api/health
curl http://localhost:5001/api/health
curl http://localhost:5002/api/health
✅ Expected responses:

json
Copy code
{"service": "product-service", "status": "ok"}
{"service": "user-service", "status": "ok"}
{"service": "order-service", "status": "ok"}
🧰 Common Commands
Action	Command
Rebuild containers	docker compose up --build
Stop containers	docker compose down
View logs	docker compose logs -f
Access shell inside container	docker exec -it <container_name> /bin/bash

🧾 Summary
3 microservices containerized individually.

Unified docker-compose.yml for orchestration.

Verified functional with /api/health endpoints.

Ready for integration with CI/CD (Task 3).

🟩 Task 2 — Dockerization: Completed Successfully

yaml
Copy code

---

## 🏗️ README.md (Update Section)

Add this section **after your CI/CD section** in the main `README.md`:

```markdown
## 🐳 Task 2 — Dockerization

This stage containerizes all three microservices (`product-service`, `user-service`, `order-service`) using Docker and Docker Compose.

### ✅ Highlights
- Each microservice has its own Dockerfile.
- Unified orchestration via `docker-compose.yml`.
- All containers run locally and communicate over exposed ports.
- Verified health endpoints for each service.

### 🔧 Commands
```bash
docker compose up --build -d
docker ps
curl http://localhost:5000/api/health
📄 Documentation
See docs/DOCKER-SETUP.md for full setup details.

yaml
Copy code

---

You’re now fully prepped to push:
```bash
git add .
git commit -m "Task 2: Dockerization setup complete"
git push origin devops/docker-setup