from pydantic import BaseModel, Field
from typing import Optional

class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="This is a name of the user",
        example='Ansh Mittal'
    )
    department: Optional[str] = 'general'
    
class Product(BaseModel):
    name: str
    price: float = Field(
        ...,
        gt=0, # gt ge
        le=1_00_000, # lt le
        description='This is a price of the product.'
    )