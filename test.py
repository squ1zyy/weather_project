def decorate(funct):
    def wrap():
        funct()
        print("Successfully wrapped functions")
    return wrap

@decorate
def func():
    print("I'm the storm...")

func()