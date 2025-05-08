lis1=[]

# for i in range(1,11):
#     if i**2%2==0:
#         lis1.append(i)
# print(lis1)

lis2=[1,2,3,4]
lis3=[]
for i in range(len(lis2)+1):
    for j in range(lis2[i]+1):
        lis3.append(i)
print(lis3)








