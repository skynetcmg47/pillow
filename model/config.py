from pydantic import BaseModel

from model.aws import AWS


class Instance(BaseModel):
    id: str
    name: str
    host_alias: str


class Config(BaseModel):
    aws: AWS
    instance: Instance
