# paramiko Module demo to fetch Isilon related information via Isilon CLI command

import paramiko

username = "root"
passwd = "a"
ip = "10.205.150.27"
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip, username=username, password=passwd)

cmd = "isi status"
stdin, stdout, stderr = ssh_client.exec_command(cmd)
for line in stdout:
    print(line)
