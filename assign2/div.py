def div(a,b):
    try:
        divi=a/b
    except ZeroDivisionError:
        print("Number is divided by Zero")

a=5
b=0
div(a,b)

def f1(fname):
    try:
        f=open(fname)
        for line in f.readline():
            print(line,end="")
    except FileNotFoundError:
        print("File not found error")


n1=input("enter file name:")
f1(n1)
