# Build app
```sh
docker-compose build
```

# Copy env
```sh
cp .env.example .env
```

# Start docker
```sh
docker-compose up
docker exec -it demo_python_app_1 bash
```

# Install dependency
```sh
pip install requirements.txt
```

# Migrate db
```sh
alembic upgrade head
```

# Start server
```sh
uvicorn src.main:app --host 0.0.0.0 --reload
```
