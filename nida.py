def add (*n):
    sum =0
    for i in n:
        sum=sum+i
    return sum 
x=eval(input("enter value"))
res=add(x)
print(res)
print(x)
print(type(x))