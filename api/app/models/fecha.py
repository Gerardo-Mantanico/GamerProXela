from pydantic import BaseModel # type: ignore


class Fecha(BaseModel):
    inicio: str
    final: str

