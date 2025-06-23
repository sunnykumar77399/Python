# convert fahrenheit to celsius

def f_to_c(f):
    return (5*(f-32)/9)

n=int(input("Enter the fohrenheit.. :"))
print(f" Degree C is {f_to_c(n)}")