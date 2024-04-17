import json
import os

from model.aws import AWS
from model.config import Config as BaseConfig


class Config:

    def __init__(self, path=None):
        if path:
            self.path = path
        else:
            self.path = f"{os.environ['HOME']}/.pillow/config.json"

    def get_config(self) -> BaseConfig:
        with open(self.path) as f:
            raw_cfg = json.loads(f.read())
            return BaseConfig(**raw_cfg)

    def get_aws_config(self) -> AWS:
        config = self.get_config()
        return config.aws

    def get_pretty_config(self):
        config = self.get_config()
        json_formatted_str = json.dumps(config.model_dump(), indent=2)
        return json_formatted_str
