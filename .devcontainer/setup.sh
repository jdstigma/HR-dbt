#!/bin/bash
set -e

echo "Installing dbt-postgres..."
pip install dbt-postgres

echo "Creating hr_db database..."
psql -U postgres -c "CREATE DATABASE hr_db;"

echo "Creating dbt profiles..."
mkdir -p ~/.dbt
cat > ~/.dbt/profiles.yml << 'EOF'
hr_dbt:
  target: dev
  outputs:
    dev:
      type: postgres
      host: localhost
      port: 5432
      user: postgres
      password: ""
      dbname: hr_db
      schema: public
      threads: 4
EOF

echo "Setup complete. PostgreSQL is running on port 5432."
