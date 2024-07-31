#To printsquare pattern with * symbols

n = int(input("Enter Number of Rows :"))
for i in range(n):
    for j in range(n):
        print("*", end='')
    print()


# : To print square pattern with provided fixed digit in every row
n = int(input("Enter No. of Rows : "))
i = 1
for i in range(n+1):
    for j in range(n):
        print(i, end='')
    print()


#  To print square pattern with alphabet symbols
n = int(input("Enter No. of Rows : "))
for i in range(n):
    for j in range(n):
        print(chr(65 + i), end=' ')
        print(chr(65 + i), end=' ')
    print()


# To print Right Angle Triangle pattern with * symbols
n = int(input("Enter No. of Rows : "))
for i in range(n+1):
    for j in range(i+1):
        print("*", end=' ')
    print()


#  To print Inverted Right Angle Triangle pattern with * symbols
n = int(input("Enter No. of Rows : "))
for i in range(n):
    for j in range(n-i):
        print("*", end=' ')
    print()



# To print Pyramid pattern with * symbols


