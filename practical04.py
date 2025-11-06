def push(stack, item):
    new_stack = []
    for i in range(strlen(stack)):
        new_stack = new_stack + [stack[i]]
    new_stack = new_stack + [item]
    return new_stack

def pop(stack):
    if strlen(stack) == 0:
        return stack, None
    new_stack = []
    for i in range(len(stack) - 1):
        new_stack = new_stack + [stack[i]]
    popped_item = stack[strlen(stack) - 1]
    return new_stack, popped_item

def strlen(s):
    count = 0
    for _ in s:
        count = count + 1
    return count

def make_change(document, undo_stack, redo_stack):
    new_text = input("Enter text to add: ")
    undo_stack = push(undo_stack, document)
    redo_stack = []
    document = document + new_text
    print("Text added to document")
    return document, undo_stack, redo_stack

def undo(document, undo_stack, redo_stack):
    if strlen(undo_stack) == 0:
        print("Nothing to undo")
    else:
        redo_stack = push(redo_stack, document)
        undo_stack, document = pop(undo_stack)
        print("Undo successful.")
    return document, undo_stack, redo_stack

def redo(document, undo_stack, redo_stack):
    if strlen(redo_stack) == 0:
        print("Nothing to redo")
    else:
        undo_stack = push(undo_stack, document)
        redo_stack, document = pop(redo_stack)
        print("Redo successful.")
    return document, undo_stack, redo_stack

def display(document):
    print("Current Document:")
    if document == "":
        print("[Empty Document]")
    else:
        print(f"{document}")

def run_editor():
    document = ""
    undo_stack = []
    redo_stack = []

    while True:
        print("1. Make a change")
        print("2. Undo")
        print("3. Redo")
        print("4. Display document")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            document, undo_stack, redo_stack = make_change(document, undo_stack, redo_stack)
        elif choice == "2":
            document, undo_stack, redo_stack = undo(document, undo_stack, redo_stack)
        elif choice == "3":
            document, undo_stack, redo_stack = redo(document, undo_stack, redo_stack)
        elif choice == "4":
            display(document)
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter number from 1 to 5 only.")
        print()

run_editor()
