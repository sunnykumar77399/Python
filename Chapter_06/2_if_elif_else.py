a=int(input("Enter a number : "))

if(a>18):
    print("you are a adult ")
    print("if condition executed")
elif(a<0):
    print("inavlide inpute")
    print("elif executed")
elif(a==0):
    print("entered wrong age ") 
else: 
    print("you are not adult\nelse executed")
print("program end")