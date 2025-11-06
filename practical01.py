M = [3, 0, 5, 2, 4, 0, 6, 1, 3, 14, 4, 0]   # books borrowed by each member
B = [2, 5, 3, 2, 5, 1, 11, 6, 4, 3, 2]  # borrow count of each book 

a = len(M)
b = len(B)

sum_books = 0
for i in range(a):
    sum_books = sum_books + M[i]
avg = sum_books / a
print("Average number of books borrowed by all members:", avg)

highest = 0
for i in range(b):
    if B[i] > highest:
        highest = B[i]
print("Highest number of times a book was borrowed:", highest)

lowest = B[0]
for i in range(1, b):
    if B[i] < lowest:
        lowest = B[i]
print("Lowest number of times a book was borrowed:", lowest)

count_zero = 0
for i in range(a):
    if M[i] == 0:
        count_zero = count_zero + 1
print("Number of members who have not borrowed any book:", count_zero)

count = []
for i in range(10):
    cnt = 0
    for j in range(b):
        if B[j] == i:
            cnt = cnt + 1
    count.append(cnt)

fb=0
for i in range(len(B)):
    if B[i]>fb:
        fb=B[i]

print("Most frequently borrowed book count is:", fb)

