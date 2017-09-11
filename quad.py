import cmath
global r1,r2
def roots(a,b,c,d):
	if(d==0):
		r1=(-b)/2*a
		r2=r1
		return print('roots are real and equal r1={0}=r2'.format(r1,r2))
	elif(d>0):
		r1=(-b+cmath.sqrt(d))/2*a
		r2=(-b-cmath.sqrt(d))/2*a
		return print ('roots are distinct r1={0} r2={1}'.format(r1,r2))
	else:
		r1=(-b+cmath.sqrt(d))/2*a
		r2=(-b-cmath.sqrt(d))/2*a
		return print('roots are complex r1={0} r2={1}'.format(r1,r2))
def read():
	return float(input())
print('enter coefficients in higher order:')
a=read()
b=read()
c=read()
d=(b*b-4*a*c)
r=roots(a,b,c,d)
print(r)
