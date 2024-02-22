# def immediate(a,n):
#     ans=-1
#     diff=100000
#     for i in a:
#         if i<a and a-i < diff:
#             ans=i
#             diff=a-i
#     return ans

# def hema(staff):
#     sum1=0
#     for i in staff:
#         sum1+=i
#         return sum1
# 
# print(hema([1,2,3,4]))

# a='  geekk s   f  h'
# out=''
# for i in a:
#     if i != " ":
#         out+=i
# print(out)

# S="HEJEhjjjjRR" 
# a=S.capitalize()
# a=a[0].lower()+a[1:]
# print(a)

# N=5
# for i in range(N):
#     for j in range(i):
#         print("*",end="")
#     print(end=" ")

# a='for'
# a[::-1]
# print(a)

arr=[2,3,4,5,1,2,3,5,7]
a=set(arr)
b=sorted(list(a))
print(b[-2])