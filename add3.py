def add(a,b,c):
    sum=float(a)+float(b)+float(c)
    return sum
a=input("enter a:")
b=input("enter b:")
c=input("enter c:")
sum=add(a,b,c)
print("sum of {0}+{1}+{2}={3}".format(a,b,c,sum))
