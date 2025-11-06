MAX_SIZE = 100
queue = [None] * MAX_SIZE
front = 0
rear = 0
size = 0

def enqueue(item):
    global rear, size
    if size == MAX_SIZE:
        print("Queue is full! Cannot add more calls.")
        return
    queue[rear] = item
    rear = (rear + 1) % MAX_SIZE
    size += 1

def dequeue():
    global front, size
    if size == 0:
        return None
    item = queue[front]
    queue[front] = None
    front = (front + 1) % MAX_SIZE
    size -= 1
    return item

def addCall(customerID, callTime):
    enqueue((customerID, callTime))

def answerCall():
    return dequeue()

def viewQueue():
    result = []
    idx = front
    count = 0
    while count < size:
        result.append(queue[idx])
        idx = (idx + 1) % MAX_SIZE
        count += 1
    return result

def isQueueEmpty():
    return size == 0

def main():
    while True:
        print("\n1. Add a call")
        print("2. Answer a call")
        print("3. View queue")
        print("4. Check if queue is empty")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            customerID = input("Enter customer ID: ")
            callTime = input("Enter call time (in minutes): ")
            if callTime.isdigit():
                addCall(customerID, int(callTime))
                print(f"Call from customer {customerID} added.")
            else:
                print("Please enter a valid number for call time.")
        elif choice == '2':
            call = answerCall()
            if call is not None:
                print(f"Answered call from customer {call[0]} ({call[1]} minutes).")
            else:
                print("No calls to answer.")
        elif choice == '3':
            q = viewQueue()
            if size > 0:
                print("Current call queue:")
                for i, (cid, ctime) in enumerate(q, 1):
                    print(f"{i}. Customer ID: {cid}, Call Time: {ctime} minutes")
            else:
                print("The call queue is empty.")
        elif choice == '4':
            print("Queue empty." if isQueueEmpty() else "Queue not empty.")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Enter number from 1 to 5.")

main()
