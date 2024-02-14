# def immediate(a,n):
#     ans=-1
#     diff=100000
#     for i in a:
#         if i<a and a-i < diff:
#             ans=i
#             diff=a-i
#     return ans

def hema(staff):
    sum1=0
    for i in staff:
        sum1+=i
        return sum1

print(hema([1,2,3,4]))
