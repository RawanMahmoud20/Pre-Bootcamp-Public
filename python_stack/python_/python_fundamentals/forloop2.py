# 1 Biggie Size

def biggie_size(num_list):
    for i in range(len(num_list)):
        if num_list[i] > 0:
            num_list[i] = "big" # Change positive values to "big"
    return  print(num_list)
biggie_size([-1 , 3 , 5 , -5])

# 2 Count Positives
def count_positives(num_list):
    count = 0
    for val in num_list:
        if val > 0:
            count += 1 # Count how many positive numbers
    
    num_list[len(num_list) - 1] = count # Replace last value with count
    return num_list
print(count_positives([-1,1,1,1]))
print(count_positives([1,6,-4,-2,-7,-2]))

# 3 Sum Total
def sum_total(num_list):
    total = 0
    for val in num_list:
        total += val # Add each value to total
    return total
print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))

# 4 Average
def average(num_list):
    total = 0
    for val in num_list:
        total += val
    return total / len(num_list) # Divide sum by the number of elements
print(average([1,2,3,4]))

# 5 Length
def length(num_list):
    # Simply return the length of the list
    return len(num_list)

print(length([37, 2, 1, -9])) # Should return 4
print(length([]))            # Should return 0
# 6  Minimum
def minimum(num_list):
    # If the list is empty, return False
    if len(num_list) == 0:
        return False
    
    min_val = num_list[0]
    for val in num_list:
        if val < min_val:
            min_val = val # Update if a smaller value is found
    return min_val

print(minimum([37, 2, 1, -9])) # Should return -9
print(minimum([]))            # Should return False
# 7. Maximum
def maximum(num_list):
    # If the list is empty, return False
    if len(num_list) == 0:
        return False
    
    max_val = num_list[0]
    for val in num_list:
        if val > max_val:
            max_val = val # Update if a larger value is found
    return max_val

print(maximum([37, 2, 1, -9])) # Should return 37
print(maximum([]))            # Should return False
# 8 Ultimate Analysis
def ultimate_analysis(num_list):
    # We can reuse our logic to build the dictionary
    result = {
        'sumTotal': sum_total(num_list),
        'average': average(num_list),
        'minimum': minimum(num_list),
        'maximum': maximum(num_list),
        'length': len(num_list)
    }
    return result

print(ultimate_analysis([37, 2, 1, -9]))

# 9 Reverse List
def reverse_list(num_list):
    # We only need to loop halfway through the list
    for i in range(len(num_list) // 2):
        # Swap the elements: first with last, second with second-to-last...
        num_list[i], num_list[len(num_list) - 1 - i] = num_list[len(num_list) - 1 - i], num_list[i]
    return num_list

print(reverse_list([37, 2, 1, -9])) # Should return [-9, 1, 2, 37]