from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
    
user = User(id=1, name="Goutam kushwah", email="abc123@gmail.com")
print(user)
print(user.name)
print(user.email)
print(user.id)

