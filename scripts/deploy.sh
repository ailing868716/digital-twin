#!/bin/bash
cd $(dirname "$0")/..
git pull origin main
docker compose down
docker compose up -d --build
