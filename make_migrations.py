import subprocess

commands = [
    "py manage.py makemigrations property_api",
    "py manage.py makemigrations reviews_api",
    "py manage.py makemigrations users_api",
    "py manage.py makemigrations authApi",
    "py manage.py makemigrations requests_api",
    "py manage.py makemigrations payment_api",
    "py manage.py migrate"
]

for command in commands:
    print(f"Executing command: {command}")
    subprocess.run(command, shell=True)

print("All commands executed successfully.")
