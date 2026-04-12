print("Python is working!")
x= "Hello Python"
y =42 
print (x , " The Number is : "+  str(y))
first_name= "Rawan"
last_name= "Mahmoud"
age = 23

print (f"My name is {first_name} {last_name} and I'm {age} years old.")
print ("Another way to print string " + "My name is {} {} and I'm {} years old.".format(first_name , last_name , age ))
# % format to you reserve 
hl ="Hello %s" % "world"
py = "I love python %d" % 3
print (hl , py)
print (f"My name is  %s %s  and I'm %d years old." % (first_name , last_name , age))
print(py.title())
print(py.capitalize())
print(py.count("o"))
print(py.upper())
print(py.lower())
print(py.split(""))
print(py.find("python"))
print(py.isalnum())
print(py.endswith("3"))