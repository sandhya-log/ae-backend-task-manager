from pydantic import BaseModel, EmailStr, field_validator

class UserCreate(BaseModel):
    email :EmailStr
    password : str

    @field_validator("password")
    @classmethod
    def validate_password_length(cls, v:str):
        if len(v.encode("utf-8")) > 72:
            raise ValueError("Password too long (max 72 characters)")
        if len(v) < 8:
            raise ValueError("Password too short (min 8 charcaters)")
        
        return v

