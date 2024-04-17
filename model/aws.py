from pydantic import BaseModel


class AWS(BaseModel):
    access_key: str
    secret_key: str
    region: str
