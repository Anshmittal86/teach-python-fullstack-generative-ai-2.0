from pydantic import BaseModel, EmailStr, HttpUrl
from typing import List, Dict, Set, Tuple, Literal
from datetime import date, time, datetime

class Employee(BaseModel):
    name: str 
    age: int
    email: str
    salary: float = 10_000.00
    is_login: bool = False
    skills: List[str]
    score: Dict[str, int] 
    tags: Set[str]
    coordinate: Tuple[float, float]
    
employee = Employee(name='aman',age=12,email='abc@gmail.com',salary=12_000, skills=["html", "css", "js", "genai"], score={ "html": 98, "css": 50, "js": 100 },tags={"html", "css", "js"},coordinate=(2.45, 5.67))


# Literal
class Person(BaseModel):
    username: str
    role: Literal['admin', 'user', 'super-admin']

person = Person(username='aman', role='user')
print(person)

# data time
class Event(BaseModel):
    event_time: time
    event_date: date
    created_at: datetime
    

# email, url
class Contact(BaseModel):
    email: EmailStr
    website: HttpUrl

# requrie pydantic[email] package
 
contact = Contact(email='aman@gmail.com', website='https://www.google.com')

print(contact)