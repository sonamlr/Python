# reverse string
name = input("Enter Strnig :")
myName = name[::-1]
print(myName)

# reverse string using reversed() function
name = input("Enter Strnig :")
r = reversed(name)
myName = ''.join(r)
print(myName)


# reverse string using while loop 
s = input("Enter String :")
n = len(s)-1
output = ''
while n >= 0:
    output = output + s[n]
    n = n -1
print(output)


# reverse words 
# input: Learning Python Is Very Easy
# output: Easy Very Is Python Learning
s = input("Enter String :")
s1 = s.split(' ')
print(s1)
s2 = s1[::-1]
output = ' '.join(s2)
print(output)

# reverse internal content of each words
# input: 'Durga Software Solutions'
# output: 'agruD erawtfoS snoituloS'
s = input("Enter String : ")
s1 = s.split(' ')
n = len(s1)
i = 0
mylist = []
while i < n:
    rev = s1[i][::-1]
    mylist.append(rev)
    i = i + 1
output = ' '.join(mylist)
print(output)


# Write a Program To REVERSE internal content of every second word present in the given string?
# i/p: one two three four five six
# o/p: one owt three ruof five xis


