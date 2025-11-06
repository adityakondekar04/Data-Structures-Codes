class Node:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
        self.next = None

class Student_Record:
    def __init__(self):
        self.head = None

    def insert(self, name, rollno, marks):
        new_node = Node(name, rollno, marks)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
        print("Data Inserted Successfully.\n")

    def display(self):
        temp = self.head
        if temp is None:
            print("No records to display.\n")
        else:
            print("Student Records:")
            while temp is not None:
                print(f"Name: {temp.name}, Roll No: {temp.rollno}, Marks: {temp.marks}", end=" -> ")
                temp = temp.next
            print("NULL\n")

    def delete(self, rollno):
        current = self.head
        if not current:
            print("List is empty.\n")
            return False

        if current.rollno == rollno:
            self.head = current.next
            print("Record deleted successfully.\n")
            return True

        prev = None
        while current and current.rollno != rollno:
            prev = current
            current = current.next

        if not current:
            print("Record not found.\n")
            return False

        prev.next = current.next
        print("Record deleted successfully.\n")
        return True

    def update(self, rollno, new_name, new_marks):
        temp = self.head
        while temp:
            if temp.rollno == rollno:
                temp.name = new_name
                temp.marks = new_marks
                print("Record updated successfully.\n")
                return True
            temp = temp.next
        print("Record not found.\n")
        return False

    def search(self, rollno=None, name=None, marks=None):
        temp = self.head
        found = False
        while temp:
            if (temp.rollno == rollno) or (temp.name == name) or (temp.marks == marks):
                print(f"Record Found: Name: {temp.name}, Roll No: {temp.rollno}, Marks: {temp.marks}\n")
                found = True
            temp = temp.next
        if not found:
            print("No matching record found.\n")
        return found

sr = Student_Record()

while True:
    print("1. Insert")
    print("2. Delete")
    print("3. Update")
    print("4. Search")
    print("5. Display")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        name = input("Enter Student Name: ")
        rollno = input("Enter Roll Number: ")
        marks = input("Enter Marks: ")
        sr.insert(name, rollno, marks)
    elif choice == "2":
        rollno = input("Enter Roll Number of the student to delete: ")
        sr.delete(rollno)
    elif choice == "3":
        rollno = input("Enter Roll Number of the student to update: ")
        new_name = input("Enter Updated Name: ")
        new_marks = input("Enter Updated Marks: ")
        sr.update(rollno, new_name, new_marks)
    elif choice == "4":
        print("Search by:\n1. Roll Number\n2. Name\n3. Marks")
        search_choice = input("Enter option (1-3): ")
        if search_choice == "1":
            rollno = input("Enter Roll Number: ")
            sr.search(rollno=rollno)
        elif search_choice == "2":
            name = input("Enter Name: ")
            sr.search(name=name)
        elif search_choice == "3":
            marks = input("Enter Marks: ")
            sr.search(marks=marks)
        else:
            print("Invalid search option.\n")
    elif choice == "5":
        sr.display()
    elif choice == "6":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please select between 1 and 6.\n")
