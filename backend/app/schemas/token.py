from pydantic import BaseModel


class TokenBase(BaseModel):
    access_token: str


class TokenCreate(TokenBase):
    user_id: int


class Token(TokenBase):
    id: int

    class Config:
        orm_mode = True
