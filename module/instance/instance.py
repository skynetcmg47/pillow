import time

from module.config.config import Config
from module.instance.aws import AWS
from module.os_process.os_process import OsProcess


class Instance:
    def __init__(self, instance_id):
        self.instance_id = instance_id
        config = Config()
        self.config = config.get_aws_config()

    def __str__(self):
        return f"Instance {self.instance_id}"

    def start(self):
        print(f"Starting instance with id {self.instance_id}")
        aws = AWS(self.config)
        client = aws.get_client("ec2")
        response = client.start_instances(
            InstanceIds=[
                self.instance_id,
            ]
        )

        instance = self.describe()
        while instance["state"] != "running":
            time.sleep(5)
            instance = self.describe()

        config = Config()
        os_process = OsProcess()
        os_process.update_instance_ip(
            config.get_config().instance.host_alias, instance["public_ip"]
        )
        return response

    def stop(self):
        print(f"Stopping instance with id {self.instance_id}")
        aws = AWS(self.config)
        client = aws.get_client("ec2")
        response = client.stop_instances(
            InstanceIds=[
                self.instance_id,
            ]
        )
        return response

    def describe(self):
        aws = AWS(self.config)
        client = aws.get_client("ec2")
        response = client.describe_instances(
            InstanceIds=[
                self.instance_id,
            ]
        )
        instance = response["Reservations"][0]["Instances"][0]
        if instance["State"]["Name"] == "running":
            rsp = {
                "id": instance["InstanceId"],
                "state": instance["State"]["Name"],
                "type": instance["InstanceType"],
                "public_ip": instance["PublicIpAddress"],
            }
        else:
            rsp = {
                "id": instance["InstanceId"],
                "state": instance["State"]["Name"],
                "type": instance["InstanceType"],
            }

        return rsp

    def instance_ip(self):
        aws = AWS(self.config)
        client = aws.get_client("ec2")
        response = client.describe_instances(
            InstanceIds=[
                self.instance_id,
            ]
        )
        return response["Reservations"][0]["Instances"][0]["PublicIpAddress"]
