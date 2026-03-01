from pydantic import BaseModel, Field, EmailStr

class User(BaseModel):
    username: str = Field(min_length=5)
    email: EmailStr
    age: int = Field(ge=18)

user_info = {"username": "john_doe", "email": "john@example.com", "age": 25}

user = User(**user_info)
print(user)