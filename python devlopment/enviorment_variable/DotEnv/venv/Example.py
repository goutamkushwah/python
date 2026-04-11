from dotenv import load_dotenv
config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}
print(config["USER"])  # foo
print(config["EMAIL"])  #
    