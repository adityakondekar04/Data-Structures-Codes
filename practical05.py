MAX_SIZE = 100
queue = [None] * MAX_SIZE
front = -1
rear = -1

def is_empty():
    return front == -1 and rear == -1

def is_full():
    return rear == MAX_SIZE - 1

def enqueue(event):
    global rear, front
    if is_full():
        print("Queue is full! Cannot add more events.\n")
        return
    if is_empty():
        front = 0
        rear = 0
    else:
        rear += 1
    queue[rear] = event

def dequeue():
    global front, rear
    if is_empty():
        return None
    event = queue[front]
    if front == rear:
        front = -1
        rear = -1
    else:
        front += 1
    return event

def add_event():
    event = input("Enter event name to add: ")
    enqueue(event)
    print(f"Event '{event}' added.\n")

def process_event():
    event = dequeue()
    if event is None:
        print("No events to process.\n")
    else:
        print(f"Event '{event}' has been processed.\n")

def display_events():
    if is_empty():
        print("No pending events.\n")
    else:
        print("Pending Events:")
        for i in range(front, rear + 1):
            print(f"{i - front + 1}. {queue[i]}")
        print()

def cancel_event():
    global front, rear, queue
    if is_empty():
        print("No events to cancel.\n")
        return

    event_name = input("Enter the name of the event to cancel: ")
    index = -1
    for i in range(front, rear + 1):
        if queue[i] == event_name:
            index = i
            break

    if index == -1:
        print(f"Event '{event_name}' not found in the queue.\n")
        return

    for i in range(index, rear):
        queue[i] = queue[i + 1]

    queue[rear] = None
    rear -= 1

    if rear < front:
        front = -1
        rear = -1

    print(f"Event '{event_name}' has been canceled.\n")

def run_event_system():
    while True:
        print("1. Add event")
        print("2. Process Next Event")
        print("3. Display Pending Events")
        print("4. Cancel Event")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_event()
        elif choice == "2":
            process_event()
        elif choice == "3":
            display_events()
        elif choice == "4":
            cancel_event()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 to 5 only.\n")

run_event_system()
