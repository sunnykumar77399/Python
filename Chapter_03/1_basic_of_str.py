a="sunny" # valid syntax
b='kumar' # valid syntax
c='''kushwaha''' # valid syntax

result=c[0:4]
print(result)

result=c[:4]
print(result)

result=c[4:]
print(result)

result=c[:]
print(result)

result=c[2:6]
print(result)

# terminal REPL code for strshort
""" 

SyntaxError: invalid syntax
>>> b="0123456789"
>>> b[0:7:3]
'036'
>>>
"""
