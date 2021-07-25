# paramiko Module demo using the ec2 instance

import paramiko

username = "ec2-user"
passwd = "Prasanth@234"
ip = "3.16.48.162"
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip, username=username, password=passwd)

cmd = "ls -lrt /home/ec2-user"
stdin, stdout, stderr = ssh_client.exec_command(cmd)
stdout = stdout.readlines()
print(stdout)

# this will produce below output from the ec2 instance
# ['total 0\n', '-rw-rw-r--. 1 ec2-user ec2-user 0 Jul 25 16:27 hello.txt\n']

# Process finished with exit code 0

