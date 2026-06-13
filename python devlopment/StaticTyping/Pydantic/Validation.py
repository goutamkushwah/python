from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: int
    name: str
    email: str
#  getting error because of email field is not in correct format    
# user = User(id="A", name="Goutam kushwah", email="abc123@gmail.com")
#  user = User(id=1, name="Goutam kushwah", email="abscs")
user = User(id=1, name="Goutam kushwah", email="abc123@gmail.com")
print(user)
print(user.name)
print(user.email)
print(user.id)

