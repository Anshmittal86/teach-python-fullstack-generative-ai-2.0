from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str

user = {
    "name": input("Enter your name: "),
    "age": int(input("Enter your age: ")),
    "email": input("Enter your email: ")
}

user_one = User(**user)

print(user_one)