from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    nickname: Optional[str] = None
    role: str = "developer"

user = {
    "name": input("Enter your name: "),
}

user_one = User(**user)

print(user_one)