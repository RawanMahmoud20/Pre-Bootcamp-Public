# --- Functions Basic I ---

#1
def a1():
    return 5
print(a1()) # Output: 5

#2
def a2():
    return 5
print(a2()+a2()) # Output: 10

#3
def a3():
    return 5
    return 10
print(a3()) # Output: 5

#4
def a4():
    return 5
    print(10)
print(a4()) # Output: 5

#5
def a5():
    print(5)
x = a5()
print(x) # Output: 5, None

#6
def a6(b,c):
    print(b+c)
# print(a6(1,2) + a6(2,3))  # (None)

#7
def a7(b,c):
    return str(b)+str(c)
print(a7(2,5)) # Output: 25

#8
def a8():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a8()) # Output: 100, 10

#9
def a9(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a9(2,3))    # Output: 7
print(a9(5,3))    # Output: 14
print(a9(2,3) + a9(5,3)) # Output: 21

#10
def a10(b,c):
    return b+c
    return 10
print(a10(3,5)) # Output: 8

#11
b = 500
print(b)
def a11():
    b = 300
    print(b)
print(b)
a11()
print(b) # Output: 500, 500, 300, 500

#12
b = 500
print(b)
def a12():
    b = 300
    print(b)
    return b
print(b)
a12()
print(b) # Output: 500, 500, 300, 500

#13
b = 500
print(b)
def a13():
    b = 300
    print(b)
    return b
print(b)
b = a13()
print(b) # Output: 500, 500, 300, 300

#14
def a14():
    print(1)
    b14()
    print(2)
def b14():
    print(3)
a14() # Output: 1, 3, 2

#15
def a15():
    print(1)
    x = b15()
    print(x)
    return 10
def b15():
    print(3)
    return 5
y = a15()
print(y) # Output: 1, 3, 5, 10


