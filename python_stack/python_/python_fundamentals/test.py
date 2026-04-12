# print("Python is working!")
# x= "Hello Python"
# y =42 
# print (x , " The Number is : "+  str(y))
# first_name= "Rawan"
# last_name= "Mahmoud"
# age = 23

# print (f"My name is {first_name} {last_name} and I'm {age} years old.")
# print ("Another way to print string " + "My name is {} {} and I'm {} years old.".format(first_name , last_name , age ))
# # % format to you reserve 
# hl ="Hello %s" % "world"
# py = "I love python %d" % 3
# print (hl , py)
# print (f"My name is  %s %s  and I'm %d years old." % (first_name , last_name , age))
# print(py.title())
# print(py.capitalize())
# print(py.count("o"))
# print(py.upper())
# print(py.lower())
# print(py.split(""))
# print(py.find("python"))
# print(py.isalnum())
# print(py.endswith("3"))


# premative data type

# is_hungry = True 
# # composite types >> Tuples 
# dog = ('Bruce', 'cocker' , 19 , False)
# if is_hungry : 
#     print(dog[0]) 
# # mutable data >> list 
# empty_list = []
ninja= ['R', 'B', 'C', 'A']
# empty_list.append(ninja)
# print(empty_list)
# # Dictionaries
# empty_dict = {}
new_person = {'name': 'John',
              'age': 38, 
              'weight': 160.2, 
              'has_glasses': False
            }
# new_person['name'] = 'Jack'
# new_person['hobbies'] = ['climbing', 'coding']
# print(new_person)
# w = new_person.pop('weight')
# print(w)
# print(new_person)

# print (type (w))
# print (type (new_person))
# print (len (new_person))
# for elem in new_person:
#     print (elem)
#     # range(start, stop, step)
# for x in range(10):
#     print(x)     
# for x in range(0, 11, 2):
#     print(x)

# for x in range(11, 0, -2):
#     print(x)    
# for i in range(0,len(ninja)):
#     print (i , ninja[i])    

# for key , value in new_person.items() :
#     print( key , ":" , value)  

  
# keys = list(new_person.keys())
# for i in range(len(keys)):
#     print(i, new_person[keys[i]])    
# 0 John
# 1 38
# 2 160.2
# 3 False

# for i in new_person.keys():
#     print(i)    
# name
# age
# weight
# has_glasses

# for i in new_person.values():
#     print(i)    

    #   while loop
# count= 0 
# while count > 5 :
#     print("looping - " , count)
#     count+=1     
# else:
#     print("Final else")    
 
# val = "string"
# x = len(val)
# i=0
# while i < x :
#     print("looping - " , val[i])
#     if  val[i] == "i":
#         break 
#     i+=1   
# else:
#     print("Final else")     
# def a( a , b):
#     return print(a+b) 
    
# print (a(2,3))  