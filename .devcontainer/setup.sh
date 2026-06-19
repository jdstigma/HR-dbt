#!/bin/bash
set -e

echo "Starting PostgreSQL..."
sudo service postgresql start

echo "Creating hr_db and setting password..."
sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'postgres';"
sudo -u postgres psql -c "CREATE DATABASE hr_db;"

echo "Creating dbt profiles.yml..."
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
      password: postgres
      dbname: hr_db
      schema: public
      threads: 4
EOF

echo "Setup complete. PostgreSQL is running on port 5432."
