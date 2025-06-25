import sys

def main():
    task = []
    options = ["1", "2", "3", "4", "5", "6"]
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice not in options:
            print("Invalid Input")
            continue
        elif choice == "1":
            add()
            display()
        elif choice == "2":
            display()
        elif choice == "3":
            remove()
        elif choice == "4":
            exit_app()
#display menu
def menu():
    print("======To-Do-List======")
    print("Add task --> '1'")
    print("View task --> '2'")
    print("Delete task --> '3'")
    print("Exit --> '4'")

#Add task
def add():
    task = input("Task: ")
    with open ("task.txt" , "a") as file:
        file.write(f"{task}\n")

#View task
def display():
    print("========TASKS========")
    with open ("task.txt", "r") as file:
        for i, line in enumerate(file, start=1):
            print(f"{i}.{line.strip()}")
    print("======================")

#Delete task
def remove():
    display()
    try:
        n = int(input("Task number to delete: ").strip())
        with open ("task.txt", "r") as file:
            lines = file.readlines()
            removed_task = lines.pop(n-1)
        with open ("task.txt", "w") as file:
            for line in lines:
                file.write(line)
        print(f"'{removed_task.strip()}' has been removed from the tasks")
        display()
    except IndexError:
        print("Input is out of range")
    except ValueError:
        print("Not an integer")

#Exit task
def exit_app():
    sys.exit()






if __name__ == "__main__":
    main()