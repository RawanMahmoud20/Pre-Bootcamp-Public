x = [ [5,2,3], [10,8,9] ]
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]=15
print(x)
students[0]['last_name']="Bryant"
print(students)
sports_directory[ 'soccer'][0]='Andres'
print(sports_directory)
z[0]['y']=30
print(z)
z[0]['vv']= z[0].pop('y')
print(z)
# Iterate Through a List of Dictionaries)

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(list):
    for the_dic in list:
        new_str=""
        for key , value in the_dic.items():
            new_str += f"{key} - {value} , "
        print(new_str[:-2])
iterateDictionary(students)     
# Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for dic in some_list:
        print(dic[key_name])
        
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

#Iterate Through a Dictionary with List Values 
dojo = {
   'locations': ['San Jose', 'gaza', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Min', 'Devon']
}

def printInfo(some_dict):
    for key, val_list in some_dict.items():
        print(f"{len(val_list)} {key.upper()}")
        for item in val_list:
            print(item)
     
        print("")
printInfo(dojo)