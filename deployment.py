import subprocess
from datetime import datetime
import os

# Create the tag and export it to the environment
tag = datetime.now().strftime("%Y%m%d%H%M%S")
os.environ["TAG"] = tag

# Define the commands
commands = [
    "git pull",
    f"docker build -t development/flask-app:{tag} .",
    "envsubst < docker-compose.yml | docker stack deploy -c docker-compose.yml flask_stack"
]

# Run the commands
for cmd in commands:
    print(f"Running: {cmd}")
    subprocess.run(cmd, shell=True, check=True, env=os.environ)
