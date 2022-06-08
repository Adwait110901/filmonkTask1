
from pydantic import BaseModel , Field ,EmailStr
#Schemas

class UserSchema(BaseModel):
    aadhar_id : int 
    email: EmailStr 
    age : int 
    
    class Config:
        extra_schema = {
            "aadhar_id":1234567891,
            "email": "dadwait@int.com",
            "age" :10  
        }

