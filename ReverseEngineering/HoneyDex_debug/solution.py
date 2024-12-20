import subprocess

command = "strings ./honeydex | grep 'TIP'"
result = subprocess.run(command, shell=True, capture_output=True, text=True)
print(result.stdout)
command = "strings ./honeydex | grep 'ZTIRPS'"
result = subprocess.run(command, shell=True, capture_output=True, text=True)
print(result.stdout)
flag = result.stdout[::-1]
print(flag)