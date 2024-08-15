import subprocess
import time

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running {command}:")
        print(result.stderr)
    else:
        print(result.stdout)

# Run `python manage.py collectstatic`
run_command('python manage.py collectstatic --noinput')

# Run `python manage.py migrate`
run_command('python manage.py migrate')

# Start the Django server
print("Starting Django development server...")

# Start the server in a non-blocking way using subprocess.Popen
server_process = subprocess.Popen(
    'python manage.py runserver',
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

# Give the server a few seconds to start
time.sleep(3)

# Print the local server link
print("Server is running at http://127.0.0.1:8000/")

# Optionally, you can capture and print the output of the server
try:
    while True:
        output = server_process.stdout.readline()
        if output == '' and server_process.poll() is not None:
            break
        if output:
            print(output.strip())
except KeyboardInterrupt:
    print("Stopping the server...")
    server_process.terminate()
