print("Equation should be in a form : ax\u00b2+bx+c=0")
a = eval(input("enter the value of a : "))
b = eval(input("enter the value of b : "))
c = eval(input("enter the value of c : "))
d = (b**2 - 4*a*c)**(1/2.0)
x1 = (b*-1 + d)/(2*a)
x2 = (b*-1 - d)/(2*a) 
print("Answer : \n x1 = %d \n x2 = %d" %(x1,x2))