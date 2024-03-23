import subprocess
import sys

commands = [
    "manage.py makemigrations property_api",
    "manage.py makemigrations reviews_api",
    "manage.py makemigrations users_api",
    "manage.py makemigrations authApi",
    "manage.py makemigrations requests_api",
    "manage.py makemigrations payment_api",
    "manage.py migrate",
]

# Determine which Python launcher to use based on the platform
python_launcher = "python3" if sys.platform != "win32" else "py"

for command in commands:
    print(f"Executing command: {command}")
    subprocess.run(f"{python_launcher} {command}", shell=True)

print("All commands executed successfully.")
