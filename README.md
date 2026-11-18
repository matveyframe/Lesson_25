1) Запустить с помощью docker приложение https://github.com/anestesia001/go-task-manager
   
 ```
services:

  postgres:
    image: postgres:18
    container_name: PostgresDB
    env_file: .env
    volumes:
      - pgdata:/var/lib/postgresql
      - ./db/init.sql:/docker-entrypoint-initdb.d/init.sql:ro
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U $${POSTGRES_USER} -d $${POSTGRES_DB}"]
      interval: 5s
      timeout: 5s
      retries: 10
    restart: unless-stopped


  app:
    image: golang:1.24-alpine
    container_name: app
    working_dir: /app
    command: sh -c "go mod tidy && go run ."
    env_file: .env
    volumes:
      - ./:/app
      - gomod:/go/pkg/mod
    ports:
      - "${APP_PORT}:8080"
    depends_on:
      postgres:
        condition: service_healthy
    restart: unless-stopped


volumes:
  pgdata:
  gomod:
```


![]( "Logo Title Text 1")

2) Написать скрипт на python, который через модуль subprocess проверяет, запущены ли контейнеры приложения

 ```
import subprocess

containers = ["PostgresDB", "app"]

result = subprocess.run(["docker", "ps", "--format", "{{.Names}}"], capture_output=True, text=True)
running = result.stdout.split()

for name in containers:
    if name in running:
        print(name, "Containers is running")
    else:
        print(name, "Containers not running")
```

![]( "Logo Title Text 1")





