#def double(x):
#    return x*2

#print(double(2))

double = lambda x:x*2
multiply = lambda x,y : x * y
add = lambda x,y,z : x+y+z
full_name = lambda first_name,last_name : first_name + last_name
ag_check = lambda age : True if age >=18 else False
print(double(5))
print(multiply(5,6))
print(add(5,6,7))
print(full_name("Tong " ,"Chin Meng"))
print(ag_check(18))