# function basic 2
# Countdown
def countDown(num):
    new_num=[]
    for i in range(num , -1 , -1):
        new_num.append(i)
        
    return (new_num)
    
result=countDown(5)
print(result)

# Print and Return 
def print_and_return(list):
    for i in range( len(list) ):
        print(list[i])
    return list[ len(list) -1]
print_and_return([1, 2])

# first plus length
def plus_first(num_list):
    value0= num_list[0]
    value_final= num_list[len(num_list)-1]
    sum = value0 +value_final
    return  print(sum)

plus_first([1,2,3,4,5])
    
# value greater than second
def  values_greater_than_second(num_list):
    if len(num_list) < 2:
        return False
    
    new_list=[]
    comparison_value = num_list[1]
    for elem in num_list:
        if(elem > comparison_value):
            new_list.append(elem)
    print("the number of value : ", len(new_list)) 
    return new_list
     
print(values_greater_than_second([5, 2, 3, 2, 1, 4]))
print(values_greater_than_second([3]))

# This length , That value
def length_and_value(size, value):
    new_list =[]
    for i in range(size):
        new_list.append(value)
    return print(new_list)

length_and_value(4,7)
length_and_value(6,2)
