try:
    age = int(input("Enter your age: "))
except ValueError as ex:
    print("Please enter a valid age")
    print(ex)
    print(type(ex))

with open("app.py") as file:
    print("File opened")
# this is a context manager
# and it will automatically close the file
