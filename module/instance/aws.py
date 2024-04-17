import boto3

from model.aws import AWS as AWSConfig


class AWS:
    def __init__(self, config: AWSConfig):
        self.access_key = config.access_key
        self.secret_key = config.secret_key
        self.region = config.region

    def __str__(self):
        return f"AWS {self.access_key} in region {self.region}"

    def get_client(self, service: str):
        return boto3.client(
            service,
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key,
            region_name=self.region,
        )
