# list1 = [1, 2, 3]
# list2 = list1
# list1.append([4, 5])
# print(list2) [1,2,3,[4,5]] [1,2,3,4,5]

# a = []
# for i in range(3):
#     a.append(i)
# a.append(a)
# print(a)

# Simulate a stack (LIFO) with a list stack = []. Perform these steps:
# Push values 10, 20, 30 onto the stack using append. [10,20,30]
# Insert 15 at index 1. [10,15,20,30]
# Pop the top element from the stack and store it in top_value. [10,15,20] top_value=[30]
# Remove the value 10 from the stack. [15,20]
# Reverse the stack. [20,15]

#
# You are building a classroom roll management tool. Students may join, leave, or be moved in the list. One student joins at the start, one leaves, two new ones join at the end, a duplicate entry is made accidentally, and finally, the last student leaves. Reverse the roll for backbench planning. You must also determine how many times a particular student appears and who left last.
# Your task: Write a Python program using appropriate list methods to manage the list of student names based on these events and print:
# The final list of students push, remove, reverse
# The student who left last pop()
# How many times a specific student appears in the list before removal count()