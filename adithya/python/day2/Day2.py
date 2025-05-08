# list_1 = [1, 2, 3]
# list_1.append(6)
# print(list_1)
#
# list_2 = [1,2,3,4,5,6,7,8,9,10]
# '''list_2.clear()
# print(list_2)'''
#
# '''list_2.sort()
# print(list_2)'''
#
# #print(list_2.index(2))
#
# list_2.insert(11,12)
# print(list_2)
#
# 1️⃣ For Loop:
# Write a for loop to append numbers 1 to 10 to an empty list.
#
# 2️⃣ While Loop:
# Use a while loop to append even numbers from 2 to 20 to a list.
#
# 3️⃣ If-Else + Append:
# Loop through numbers 1–10 and append 'odd' or 'even' to a list accordingly.
#
# 4️⃣ Continue Statement:
# Loop from 1 to 15, append numbers to a list, but skip numbers divisible by 3 (use continue).
#
# 5️⃣ Break Statement:
# Loop through numbers 1–10, append them to a list, and break the loop if the number is 5.
#
# 6️⃣ Function + Append:
# Create a function that takes a list and a number n, and appends n to the list.
#
# 7️⃣ Nested Loop:
# Use a nested for loop to create a list of lists, each containing numbers from 1 to 3.
#
# 8️⃣ Pass Statement:
# Write a loop that appends positive numbers to a list, and uses pass if a number is zero or negative.
#
# 9️⃣ Combo Challenge:
# Loop through numbers 1–20, and append numbers that are either even or multiples of 5.
#
# 🔟 Do-While Simulation:
# Simulate a do-while loop to keep appending numbers to a list until its length reaches 5.

lis1 = []
for i in range(1,11):
    lis1.append(i)
print(lis1)

for i in range(2,20):
    if i % 2 == 0:
        lis1.append(i)
print(lis1)
i = 2
while i<=20:
    if i % 2 ==0:
        lis1.append(i)
    i += 1
print(lis1)

i = 0

for i in range(1,10):
    if i % 2 == 0:
        lis1.append("even")

    else:
        lis1.append("odd")
# i += 1
print(lis1)
# i = 1
for i in range(1,15):
    if i % 3 != 0:
        lis1.append(i)

    else:
        continue
    # i += 1
print(lis1)

i = 1
for i in range(1,10):
    if i==5:
        break
    else:
        lis1.append(i)
    i += 1
print(lis1)

lis2 = [1,2,3]
lis3 = [1,2,3]
for i in range(3):
    for j in lis3:
        lis2.append(j)
print(lis2)

i2 = [-1, 1, 2, -2, 5, 0]
for i in i2:

    if i > 0:
        lis1.append(i)
    else:
        pass
        i += 1
print(lis1)

for i in range(20):
    if i % 2 == 0:
        lis1.append(i)
    elif i % 5 == 0:
        lis1.append(i)
    else:
        pass
print(lis1)

i = 0

while True:
    lis1.append(i)
    i +=1

    if len(lis1) == 5:
        break
print(lis1)

def append_number(my_list, n):
    my_list.append(n)
    return my_list
