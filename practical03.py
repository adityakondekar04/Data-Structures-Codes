
salaries = []
n=int(input("Enter number of employees: "))
for i in range(n):
    sal=int(input(f"Enter salary of employee {i+1}: "))
    salaries.append(sal)
print(f"Original Salaries:{salaries}")

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

choice=int(input("Choose sorting method: \n1 for Selection Sort\n2 for Bubble Sort\n "))
if choice==1:
    sorted_salaries = selection_sort(salaries)
    print("\nSalaries after Selection Sort (Ascending):")
    print(sorted_salaries)
elif choice==2:
    sorted_salaries = bubble_sort(salaries)
    print("\nSalaries after Bubble Sort (Ascending):")
    print(sorted_salaries)
else:
    print("Invalid choice")

selection_sorted = selection_sort(salaries)
print("\nTop 5 Highest Salaries in the Company:")
for s in selection_sorted[-5:][::-1]:
    print(s)
