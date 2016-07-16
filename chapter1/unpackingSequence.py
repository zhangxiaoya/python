
print ("Unpcking a list")
p=(4,5)
x,y = p
print (x)
print (y)

data =['ACME',50,91.1,(2012,12,21)]
name ,shares,price,date = data
print (name)
print (shares)
print (price)
print (date)


# a,b,c =(4,5)
# print a,c,c

print ("Unpacking a string")
s = "hello"
a,b,c,d,e =s
print (a,b,c,d,e)

_,share,price,_=data
print (share)
print (price)