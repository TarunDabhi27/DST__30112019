#Before Python executes any section of the code it sets few special variable
#__init__ is one of them
#print("First Module name is {} ".format(__name__))


#def main_method():
#    print("Module is main")


if __name__ == "__main__":
    print("Run Directly")
else:
    print("Run from Import")

