import subprocess
import socket

image_path = 'C:\\Users\\A508\\ilegac\\LAB-1\\imageFESB.001'

bitlocker2john_cmd = f'bitlocker2john -i {image_path}'
process = subprocess.Popen(bitlocker2john_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
output, error = process.communicate()
keys = output.decode().strip().split('\n')
recovery_key = [s for s in keys if "$bitlocker$1$" in s]
hashcat_cmd = f'hashcat -m 22100 -a 3 {recovery_key[0]} "218?d?d?d?d?d"'
process = subprocess.call(hashcat_cmd, shell=True)

cracked_password = subprocess.check_output([hashcat_cmd + " --show"], shell=True).decode()
cracked_password = cracked_password.split(':')[-1]

print(f'Recovery: {recovery_key[0]}')
print(f"PASSWORD : {cracked_password}")