#!/usr/bin/env sh
set -e

cd "$(dirname "$0")"

if [ ! -f .venv/bin/activate ]; then
  echo "Error: .venv not found. Create the virtual environment with 'python3 -m venv .venv'."
  exit 1
fi

# shellcheck source=/dev/null
. .venv/bin/activate

python manage.py runserver
