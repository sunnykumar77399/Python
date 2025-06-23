n=int(input("Enter a number : "))
i=2

while(n%i!=0 and i<n):
    # print(f"{n}*{i}={n*i}")
    i+=1
if(i==n):
    print(f"{n} is prime number")
else:
    print("not prime number")


