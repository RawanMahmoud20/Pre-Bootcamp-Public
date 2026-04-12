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
