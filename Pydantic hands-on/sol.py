from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Address(BaseModel):
    city: str = Field(min_length=3)
    pincode: str = Field(pattern=r'^\d{6}$') 

class User(BaseModel):
    user_id: int
    name: str
    email: EmailStr
    age: int = Field(ge=18)
    address: Address
    is_premium: Optional[bool] = False

user_info = {
    "user_id": 1, 
    "name": "John Doe",
    "email": "john.doe@example.com",
    "age": 25,
    "address": {
        "city": "New York",
        "pincode": "100001"
    },
    "is_premium": True
}

user = User(**user_info)
user_dict = user.dict()
print(user_dict)