from app.types.base import BaseInputModel
import hashlib
from pydantic import field_validator
import re


class UserInputModel(BaseInputModel):
    username: str
    email: str
    password: str
    is_superuser: bool = False

    @property
    def hashed_password(self) -> str:
        # Simple SHA256 hash for demonstration; use passlib in production!
        return hashlib.sha256(self.password.encode("utf-8")).hexdigest()

    @field_validator("password")
    def validate_password_strength(cls, v):
        # Example criteria: min 8 chars, upper, lower, digit, special char
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not re.search(r"[A-Z]", v):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"[a-z]", v):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search(r"\d", v):
            raise ValueError("Password must contain at least one digit")
        if not re.search(r"[^\w\s]", v):
            raise ValueError("Password must contain at least one special character")
        return v
