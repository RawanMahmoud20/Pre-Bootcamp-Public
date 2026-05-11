from collections import deque, Counter

def first_non_repeating(stream):
    queue = deque()   # tracks order
    count = {}        # tracks frequency 
    result = []  

    for char in stream:
        # count frequency
        count[char] = count.get(char, 0) + 1
        queue.append(char)

        # remove repeating from front
        while queue and count[queue[0]] > 1:
            queue.popleft()

        # first non-repeating
        if queue:
            result.append(queue[0])
        else:
            result.append(None)

    return result

stream = "aabcbbc"
string1="uubcc"
print(first_non_repeating(string1))

print(first_non_repeating(stream))
# ['a', None , 'b', 'c', 'c', 'c', None] 

