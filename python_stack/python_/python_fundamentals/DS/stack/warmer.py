def days_until_warmer(temps):
    result = [0] * len(temps)
    stack =[]   # store index
    
    for i in range(len(temps)):
        while stack and temps[i] > temps[stack[-1]]:
            idex = stack.pop()
            result[idex]= i-idex
        stack.append(i)
        
    return  result
    

temps = [22, 18, 28, 32, 25, 20, 23]
print(days_until_warmer(temps)) 
 
