import subprocess


class OsProcess:
    def __init__(self):
        pass

    def run(self, command):
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        process.wait()
        return process.returncode, process.stdout.read(), process.stderr.read()

    def update_instance_ip(self, name, ip):
        with open("/etc/hosts", "r") as file:
            filedata = file.readlines()
            for i in range(len(filedata)):
                if name in filedata[i]:
                    filedata[i] = f"{ip} {name}\n"
        with open("/etc/hosts", "w") as file:
            file.writelines(filedata)
