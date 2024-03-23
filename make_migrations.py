import subprocess

commands = [
    "python3 manage.py makemigrations property_api",
    "python3 manage.py makemigrations reviews_api",
    "python3 manage.py makemigrations users_api",
    "python3 manage.py makemigrations authApi",
    "python3 manage.py makemigrations requests_api",
    "python3 manage.py makemigrations payment_api",
    "python3 manage.py migrate"
]

for command in commands:
    print(f"Executing command: {command}")
    subprocess.run(command, shell=True)

print("All commands executed successfully.")
