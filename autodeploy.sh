#!/bin/bash

cd ~/apps/mindx-auto-feedback

echo "Pulling latest code..."
git pull

echo "Building new Docker image..."
docker build -t mindx-auto-feedback .

echo "Stopping old container..."
docker stop mindx-auto-feedback || true
docker rm mindx-auto-feedback || true

echo "Starting new container..."
docker run -d --name mindx-auto-feedback --env-file .env -p 8501:8501 mindx-auto-feedback

echo "Deploy complete!"
