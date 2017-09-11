def add(a):
    sum=0
    for i in a:
     sum=sum+i
    return sum
a=input("enter the elements\n")
n=[int(x) for x in a.split()] 
sum=add(n)
print("the sum is {0}".format(sum))
