def first_largest(a):
    if len(a)==1:
        return a
    else:
        max1=a[0]
        for i in range(1,len(a)):
            if a[i]>max1:
                max1=a[i]
    return max1

print(first_largest([2,3,1,12,4,7,9,2,1]))
