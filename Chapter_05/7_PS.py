d={}
count=0
while(count!=5):
    name=input("Enter the name : ")
    lang=input("Enter language name : ")
    d.update({name:lang})
    count=count+1

print(d)
print(type(d))
