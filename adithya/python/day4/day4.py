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

# stack = []
# stack.append(10)
# stack.append(20)
# stack.append(30)
# # print(stack)
# stack.insert(1,15)
# top_value = stack.pop()
# stack.remove(10)
# stack.reverse()
# # print(top_value)
# print(stack)

#
# You are building a classroom roll management tool. Students may join, leave, or be moved in the list. One student joins at the start, one leaves, two new ones join at the end, a duplicate entry is made accidentally, and finally, the last student leaves. Reverse the roll for backbench planning. You must also determine how many times a particular student appears and who left last.
# Your task: Write a Python program using appropriate list methods to manage the list of student names based on these events and print:
# The final list of students push, remove, reverse
# The student who left last pop()
# How many times a specific student appears in the list before removal count()

# student_login = []
# student_famous = ["chotu","bios"]
# student_login.append(["semi", "flash","msemi"])
# # student_login.pop()
# student_login.extend(student_famous)
# student_login.append("semi")
# # student_login.pop()
# student_login.reverse()
# print(student_login.count("semi"))
# print(student_login)


# Question 1: Library Book Inventory
# A library keeps a list of book titles available for borrowing. Every day, new books are added, some are removed when borrowed, and duplicates need to be handled.
#
# Your task:
#
# Start with a predefined list of book titles.
#
# For each book in a separate “borrowed” list, remove it from the main list if it exists.
#
# Add new books from an "incoming shipment" list using a loop.
#
# Count how many times a specific book appears.
#
# Reverse the final list and display the inventory.
#
# You should print:
#
# Final list of books
#
# Number of times a specific book appeared


# titles =["GOT","Stranger things","Harry potter","Atomic habits"]
# borrowed =["GOT", "Harry potter"]
#
# # for title in titles:
# #     if title in borrowed:
# #         titles.remove(title)
# # print(titles)
#
# # for titl in borrowed:
# #     print(titl)
#
# incoming_shipment = ["spiderman", "batman", "superman"]
#
# for ti in incoming_shipment:
#     titles.append(ti)
# print(titles)
#
# titles.extend(borrowed)
# print(titles)
#
# print(titles.count("GOT"))
#
# titles.reverse()
# print(titles)

# Question 2: Class Topper Finder
# You are given a list of student names along with their scores in two separate lists:
#
# python
# Copy
# Edit
names = ["Amit", "Sita", "Ravi", "Zara"]
scores = [85, 92, 88, 91]
# Your task:
#
# Use a loop to find the name of the highest scorer.
# lowest_score_index = scores.index(min(scores))
# print(names[lowest_score_index])

lowest_score_index = 0
for i in range(0, len(names)):
    if scores[i] < scores[lowest_score_index]:
        lowest_score_index = i
scores.pop(lowest_score_index)
names.pop(lowest_score_index)
print(names)
print(scores)
# Remove the student with the lowest score from both lists.

#
# Insert a new student and their score at the beginning of the list.
names.insert(0,"semi")
scores.insert(0,90)
print(names)
print(scores)
#
# Extend the list with a new batch of students and scores.
names_2 = ["Amita", "Sitan", "RaviM", "Zarakhan"]
scores_2 = [80, 98, 78, 98]
names.extend(names_2)
scores.extend(scores_2)
print(names)
print(scores)
# Reverse the name list for seat allotment.
names.reverse()
scores.reverse()
print(names)
print(scores)
# You should print:
#
# Name of the topper
highest_score_index = 0
for i in range(0, len(names)):
    if scores[i] > scores[highest_score_index]:
        highest_score_index = i
# print(scores.pop(highest_score_index))
print(names[highest_score_index])

# Final student list
print(names)
print(scores)
# Final score list

# ✅ Question 3: Order Processing System
# You're managing an order queue in an online shop. Orders come in as a list of order IDs. Some get canceled, some are delivered (popped), and new ones keep coming.
#
# Your task:
#
# Process orders in a while loop: pop and mark as “delivered” until the queue is empty or a specific stop ID is found.
#
order_queue = [101, 102, 103, 104, 105]
stop_id = 104
new_orders = [106, 107, 102, 108]

delivered_orders = []

while order_queue:
    current = order_queue.pop(0)
    if current == stop_id:
        break
    delivered_orders.append(current)

# Append new orders from another list.
#
order_queue.extend(new_orders)
# Remove any duplicate order IDs from the queue.
#
seen = set()
final_queue = []
for order in order_queue:
    if order not in seen:
        final_queue.append(order)
        seen.add(order)
print( final_queue)

# Display the number of orders processed.
print("Orders Processed:", len(delivered_orders))
# You should print:
#
print("Delivered Orders:", delivered_orders)
print("Pending Orders:", final_queue)

# List of delivered orders
#
# Final list of pending orders

# ✅ Question 4: Voting System Validator
# You are validating votes in a list of voter IDs. Some voter IDs are invalid (appear more than once), and some are missing from the expected range.
#
# Your task:
#
# Given a list of voter IDs (integers), use a loop to count how many duplicates exist.
#
voter_ids = [1, 2, 3, 2, 4, 5, 6, 3, 7, 8, 9, 10, 10, 1]
duplicates = 0
unique_voters = []
for vid in voter_ids:
    if vid not in unique_voters:
        unique_voters.append(vid)
    else:
        duplicates += 1
# Remove duplicates using list methods.
#
# Check using a loop which voter IDs from range(1, 11) are missing.
unique_voters.append(11)
# Insert a missing voter ID manually.
missing_ids = []
for i in range(1, 11):
    if i not in unique_voters:
        missing_ids.append(i)
# You should print:


print("Duplicate votes found:", duplicates)
print("Final cleaned voter list:", unique_voters)
print("Missing voter IDs:", missing_ids)
# Number of duplicate votes found
#
# Final cleaned voter list
#
# List of missing voter IDs











