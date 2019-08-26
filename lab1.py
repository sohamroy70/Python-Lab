print ("Hi, I am Varsha Roxan")

a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
print ("Addition of {} and {} is {}".format(a,b,a+b))
print ("Addition of",a,"and",b,"is",(a+b))

print (2+3)
print (2-3)
print (2/3)
print (2%3)
print (2//3)

print (2*3/5)
print (2+3*6)

course = "python programming"
print (course.upper())
print (course.replace("python","java"))

print (course[0:6])
print (len(course))
print (course[5])

a = " lab"
print (course+a)

b = '"CMR" "University"'
print (b)

#Swapping
a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = a
a = b
b = c
print ("After swapping: \na =",a,"\nb=",b)

#Fibonacci
length = int(input("Enter the value:"))
x = 0
y = 1
iteration = 0
if length <= 0:
   print("Please provide a number greater than zero")
elif length == 1:
   print("This Fibonacci sequence has {} element".format(length), ":")
   print(x)
else:
   print("This Fibonacci sequence has {} elements".format(length), ":")
   while iteration < length:
       print(x, end=', ')
       z = x + y
       x = y
       y = z
       iteration += 1
