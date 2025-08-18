# Stage 1: Build React frontend
FROM node:18 AS builder
WORKDIR /app
COPY frontend ./frontend
RUN cd frontend && npm install && npm run build

# Stage 2: Final image
FROM python:3.11-slim
WORKDIR /app
RUN apt-get update && apt-get install -y nginx && rm -rf /var/lib/apt/lists/*
COPY backend/ ./backend/
COPY --from=builder /app/frontend/build ./frontend/build
COPY nginx.conf /etc/nginx/nginx.conf
COPY start.sh /start.sh
RUN chmod +x /start.sh
RUN pip install --no-cache-dir -r backend/requirements.txt
EXPOSE 5000
CMD ["/start.sh"]
