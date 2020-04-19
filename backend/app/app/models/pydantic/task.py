from typing import Optional
from pydantic import BaseModel

class Task(BaseModel):
    name: str
    enabled: bool
    method: str
    url: str
    data: Optional[str] = None
    success_result : Optional[str] = None
    user: str
