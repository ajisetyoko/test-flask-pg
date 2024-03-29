# Wait PostgreSQL

# Start Service
flask db upgrade && gunicorn -b 0.0.0.0 'app:app'