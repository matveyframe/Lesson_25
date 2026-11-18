import subprocess

containers = ["PostgresDB", "app"]

result = subprocess.run(["docker", "ps", "--format", "{{.Names}}"], capture_output=True, text=True)
running = result.stdout.split()

for name in containers:
    if name in running:
        print(name, "Containers is running")
    else:
        print(name, "Containers not running")
