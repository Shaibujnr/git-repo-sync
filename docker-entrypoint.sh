#!/bin/sh

set -e

. /venv/bin/activate

while ! alembic upgrade head
do
     echo "Retry..."
     sleep 1
done

exec uvicorn git_repo_sync.app:app --reload --workers 1 --host 0.0.0.0 --port $PORT
