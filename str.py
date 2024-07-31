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
s = input("Enter String : ")
words = s.split()
n = len(words)
i = 0
l = []
while i < n:
    if i % 2 == 0:
        l.append(words[i])
    else: 
       
       l.append(words[i][::-1])
    i  += 1
output = ' '.join(l)
print(output)


#  Write a program to print the characters present at even index and odd index seperately for the given string?
s = input("Enter String : ")
print("Even Indexes")
n = len(s)
i = 0
j = 1
while n > i:
    if i%2 == 0:
        print(i)
    i += 2
print("Odd Indexes")
while n > j:
    if j%2 != 0:
        print(j)
    j += 2


#  Write a program to merge characters of 2 strings into a single string by taking characters alternatively?
# Input: s1='RAVI', s2='TEJA'
#  Output: RTAEVJIA

# if string are same length
s1 = 'RAVI'
s2 = 'TEJA'
l = []
if len(s1) == len(s2):
    for i in range(len(s1)):
        l.append(s1[i] + s2[i])
output = ''.join(l)
print(output)

# if string are different length
s1 = 'SONAM'
s2 = 'RAJPUT'
i,j = 0, 0
output = ''
while len(s1)>i or len(s2)>j:
    if len(s1)>i:
        output = output + s1[i]
        i += 1
    if len(s2)>j:
        output = output + s2[j]
        j += 1
print(output)


# Assume input string contains only alphabet symbols and digits.Write a program to sort characters of the string,
# first alphabet symbols followed by digits?
s =  'B4A1D3'
# output: 'ABD134'
digits = []
alphabets = []
for i in s:
    if i.isalpha():
        alphabets.append(i)
    else:
        digits.append(i)

output = ''.join(sorted(alphabets) + sorted(digits))
print(output) 

#####################################################################


#input: a4b3c2
# output: aaaabbbcc
s  = 'a4b3c2'
output = ''
for ch in s:
    if ch.isalpha():
        x = ch
    else:
        d = int(ch)
        output = output + (x*d)
print(output)

########################################################################


# input: a3z2b4
# output: aaabbbbzz
s = 'a3z2b3'
output = ''
for ch in s:
    if ch.isalpha():
        x = ch
    else:
        d = int(ch)
        output = output + (x*d)
ans = ''.join(sorted(output))
print(ans)


########################################################################


# input: aaaabbbccz
# output: 4a3b2c1z

# s = 'aaaabbbccz'




########################################################################

# Write a program for the following requirement?
# Input: a4k3b2
# Output: aeknbd
s = 'a4k3b2'
output = ''
for ch in s:
    if ch.isalpha():
        x = ch
        output = output + ch 
    else:
        d = int(ch)
        output = output + chr(ord(x) + d)
print(output)

########################################################################################

#  Write a program to remove duplicate characters from the given
#  input String?
#  Input: AZZZBCDABBCDABBBBCCCCDDDDEEEEEF
#  Output: AZBCDEF

s = 'AZZZBCDABBCDABBBBCCCCDDDDEEEEEF'
ans = ''
rev = set(s)
output = ''.join(sorted(rev))
print(output)
#----------------------------------------------------------
for ch in s:
    if ch not in ans:
        ans = ans + ch 
print(ans)


#######################################################################################################

# Write a program to find the number of occurrences of each
#  character present in the given string?
s = 'ABCDABXXXBCDABBBBCCCZZZZCDDDDEEEEEF'
d = dict()
for ch in s:
    if ch not in d:
        d[ch] = 1
    else:
        d[ch] += 1
print(d)

# Write the program for the following requirement:
#  Input: ABAABBCA
#  Output: 4A3B1C

s = 'ABAABBCA'
d = dict()
output = ''
for ch in s:
    if ch not in d:
        d[ch] =  1 
    else:
        d[ch] += 1
for k,v in d.items():
    output = output + str(v) + k 
print(output)

# Write a program to find the number of occurrences of each vowel present in the given string?
s = input("Enter String : ")
vowels = ['a','e','i','o','u','A','E','I','O','U']
d = dict()
for ch in s:
    if ch in vowels:
        if ch not in d:
            d[ch] = 1
        else:
            d[ch] += 1
print(d)

# Write a program to check whether the given two strings are anagrams or not?
s1 = 'zaly'
s2 = 'lazy'
if sorted(s1) == sorted(s2):
    print('Armstrong')
else:
    print("Not Armstrong")


# Write a program to check whether the given string is palindrome or not ?
s = input("Enter string : ")
if s == s[::-1]:
    print("Palindrom")
else:
    print("Not Palindrom")

# Write the program for the following requirement:
# inputs:
s1='abcdefg'
s2='xyz'
s3='12345'
# output: ax1, by2,cz3,d4,e5,f,g



i=j=k = 0
while i<len(s1) or j<len(s2) or k<len(s3):
    output = ''
    if i<len(s1):
        output = output + s1[i]
        i += 1
    if j<len(s2):
        output = output + s2[j]
        j += 1
    if k<len(s3):
        output = output + s3[k]
        k += 1
    print(output)






  













