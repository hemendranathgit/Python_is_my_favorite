# in pattrens we have nested loops
# for the outer loop.count the no.of lines
#for the inner loop, focus on the columns and connect them some how to the rows
# what ever your printing print them inside the inner for loop
#observe the symmetry
'''
def square(n):
    for i in range(n):
        for j in range(n):
            print("*",end=" ")
        print()
square(5)

def right_triangle(n):
    for i in range(n):
        for j in range(i+1):
            print('*', end=" ")
        print()
right_triangle(5)

def inverted_right_pyramid(n):
    for i in range(n):
        for j in range(n-i):
            print('*', end=" ")
        print()
inverted_right_pyramid(5)


def triangle(n):
    for i in range(n):
        # space
        for j in range(n-i):
            print(" ",end=" ")
        for k in range(2*i+1):
            print("*",end=" ")
        for j in range(n-i):
            print(" ",end=" ")
        print()
triangle(5)

def inverted_triangle(n):
    for i in range(n):
        # space
        for j in range(i):
            print(" ",end=" ")
        for k in range(2*(n-i)-1):
            print("*",end=" ")
        for j in range(i):
            print(" ",end=" ")
        print()
inverted_triangle(5)

def diamond(n):
    for i in range(n):
        # space
        for j in range(n - i-1):
            print(" ", end=" ")
        for k in range(2 * i + 1):
            print("*", end=" ")
        for j in range(n - i-1):
            print(" ", end=" ")
        print()
    for i in range(n):
        # space
        for j in range(i):
            print(" ",end=" ")
        for k in range(2*(n-i)-1):
            print("*",end=" ")
        for j in range(i):
            print(" ",end=" ")
        print()
diamond(5)


def forward_triangle(n):
    for i in range(2*n):
        stars=i
        if (i>n):
            stars=2*n-i
        for j in range(stars):
            print("*",end=" ")
        print()
forward_triangle(5)
'''

def one_zero(n):
    for i in range(n):
        for j in range(i+1):
            a=1
            print(a,end=" ")
            a=0
        print()

one_zero(5)