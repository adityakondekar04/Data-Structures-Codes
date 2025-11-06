customers = [101, 203, 305, 409, 512, 618, 725, 834, 910]

# Linear Search
def linear_search(customers, key):
    for i in range(len(customers)):
        if customers[i] == key:
            return i  # return index if found
    return -1  # not found

# Binary Search
def binary_search(customers, key):
    low = 0
    high = len(customers) - 1
    while low <= high:
        mid =int( (low + high)/2)
        if customers[mid] == key:
            return mid
        elif customers[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print("Customer IDs:", customers)
key = int(input("Enter Customer ID to search: "))
choice=int(input("Choose search method: \n1 for Linear Search\n2 for Binary Search\n "))   
if choice==1: 
    demo1 = linear_search(customers, key)
    if demo1 != -1:
        print("Linear Search: Customer found at position", demo1 + 1)
    else:
        print("Linear Search: Customer not found")
elif choice==2:
    demo2 = binary_search(customers, key)
    if demo2 != -1:
        print("Binary Search: Customer found at position", demo2 + 1)
    else:
        print("Binary Search: Customer not found")
else:
    print("Invalid choice")
