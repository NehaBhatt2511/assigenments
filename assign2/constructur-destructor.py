class test:
    def __init__(self):
        print("constructor")

    def __del__(self):
        print("Destructor")


if __name__ =="__main__":
    obj = test()
    del obj


