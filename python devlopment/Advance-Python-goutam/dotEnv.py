from dotenv import load_dotenv
config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}
print(config["USER"])  # foo
print(config["EMAIL"])  #
    
# code put in enviorment vaiable and run that code
#download package
