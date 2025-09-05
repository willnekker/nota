# Stage 1: Build the React frontend
FROM node:20-alpine as frontend-builder

WORKDIR /app/frontend

COPY ./frontend/package.json ./frontend/package-lock.json ./frontend/
RUN npm install --frozen-lockfile

COPY ./frontend/ ./ 
RUN npm run build

# Stage 2: Build the FastAPI backend and install Whisper
FROM python:3.10-slim-buster as backend-builder

WORKDIR /app/backend

# Install system dependencies for Whisper and psycopg2
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libpq-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY ./backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./backend/ ./

# Stage 3: Final image
FROM python:3.10-slim-buster

WORKDIR /app

# Install system dependencies for Whisper and psycopg2
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy backend from backend-builder
COPY --from=backend-builder /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
COPY --from=backend-builder /app/backend /app/backend

# Copy frontend build from frontend-builder
COPY --from=frontend-builder /app/frontend/build /app/frontend/build

# Install Nginx for serving frontend
RUN apt-get update && apt-get install -y nginx && rm -rf /var/lib/apt/lists/*

# Nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 8080

CMD ["/bin/bash", "-c", "service nginx start && uvicorn backend.app.main:app --host 0.0.0.0 --port 8000"]