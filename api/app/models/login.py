from pydantic import BaseModel # type: ignore
from typing import Optional

class Login(BaseModel):
    email: str
    password: str
