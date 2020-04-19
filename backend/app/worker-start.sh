#! /usr/bin/env bash
set -e

cd /app/app

celery worker -A worker -l info -Q main-queue -c 1
