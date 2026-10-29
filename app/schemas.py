from typing import Annotated

from pydantic import BaseModel, EmailStr, Field, StringConstraints

#Below here code is not given in the exam. Libraries given are "from typing import Annotated" and "from pydantic import BaseModel".

class UserCreate(BaseModel): 
    user_id: int = Field(gt=0) 
    name: Annotated[str, StringConstraints(min_length=2, max_length=50)] #means: name is a string, but it must follow extra validation rules. 
    email: EmailStr 
    age: int = Field(gt=18, lt=120) 
    student_id: Annotated[str, StringConstraints(pattern=r"^S\d{7}$")] #means: student_id is a string, but it must match a specific pattern.