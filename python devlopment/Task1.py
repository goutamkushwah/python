# validate user inout excersisecise
# user name is no than 12 character
# user name not contain spaces
# user name not contain digit

username= input("Enter your user name: ")
if len(username) > 12:
    print("User name should not be greater than 12 character")
elif " " in username:
    print("User name should not contain spaces")
elif any(char.isdigit() for char in username):

    print("User name should not contain digits")
else:
    print("Valid user name")