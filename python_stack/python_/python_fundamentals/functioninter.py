import random
def randInt(min=0 , max=100):
    # random.random() * (max - min) + min
    # return round(num)  # convert from . to int 
    return  random.randint(min, max)
  
print(randInt()) 		            
print(randInt(max=50)) 	          
print(randInt(min=50)) 	   
print(randInt(min=50, max=500))