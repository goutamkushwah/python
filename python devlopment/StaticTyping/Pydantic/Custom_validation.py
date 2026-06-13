from pydantic import BaseModel , EmailStr, validator

class User(BaseModel):
    id: int
    name: str
    email: str
    @validator("id")
    def id_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('ID must be a positive integer')
        return v
# user = User(id=-1, name="Goutam kushwah", email="abc123@gmail.com") 
user = User(id=1, name="Goutam kushwah", email="abc123@gmail.com")
print(user)
print(user.name)
print(user.email)
print(user.id)


# user = User(id=-1, name="Goutam kushwah", email="abc123@gmail.com")
user = User(id=1, name="Goutam kushwah", email="abc123@gmail.com")
print(user)
print(user.name)
print(user.email)
print(user.id)