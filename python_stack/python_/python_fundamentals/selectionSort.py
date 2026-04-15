
def selectionSort(arr):
    for i in range(len(arr)):
        min_i= i
        for j in range(i+1 , len(arr)):
            if arr[j] < arr[min_i]:  
               min_i = j    
   
        arr[i] , arr[min_i] = arr[min_i] , arr[i]
    return arr




num= [55,64,67,78,20,23,34,80,10,88,99]  
print(f"befor sort : {num}") 
selectionSort(num)
print(f"after sort : {num}") 
