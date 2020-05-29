n = int(input("enter number"))
count = 0
n1 = 0
n2 = 1



if n < 0:
        print("Incorrect input")

elif n == 1:
        print("0")

elif n == 2:
        print("0")
        print("1")
else:
        while count < n:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1





  
  