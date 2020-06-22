# Executing Shell Commands With subprocess.run
import subprocess
proc = subprocess.run(['ls', '-l'])
print(proc)
proc = subprocess.run(
    ['ls'],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)
print(proc)
print(proc.stdout)
print(proc.stdout.decode())

# Intentionally Raising Errors
new_proc = subprocess.run(['cat', 'fake.txt'])
print(new_proc)
