import json


def clearPrevOutput() -> None:
    import os

    os.system("cls")


def read_file(filename="local.json") -> list:
    with open(filename, "r") as f:
        return json.load(f)


def write_file(data: list, filename="local.json") -> None:
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)


def showOutput() -> None:
    for group in read_file():
        for category, tasks in group.items():
            print(category.capitalize())
            print(*[f"\t{t.capitalize()}" for t in tasks], sep="\n")


def addCategory() -> None:
    data = read_file()
    name = input("Enter new category name: ").strip().lower()
    if any(name in group for group in data):
        print("Category already exists!")
    else:
        data.append({name: []})
        write_file(data)
        clearPrevOutput()
        print(f'Category "{name}" added!')


def removeCategory() -> None:
    data = read_file()
    name = input("Enter category name to remove: ").strip().lower()
    new_data = [group for group in data if name not in group]
    if len(new_data) == len(data):
        print("Category not found!")
    else:
        write_file(new_data)
        clearPrevOutput()
        print(f'Category "{name}" removed!')


def addTask() -> None:
    data = read_file()
    name = input("Enter category name: ").strip().lower()
    task = input("Enter new task: ").strip().lower()
    for group in data:
        if name in group:
            group[name].append(task)
            write_file(data)
            clearPrevOutput()
            print(f'Task "{task}" added under "{name}"!')
            return
    print("Category not found!")


def removeTask() -> None:
    data = read_file()
    name = input("Enter category name: ").strip().lower()
    task = input("Enter task to remove: ").strip().lower()
    for group in data:
        if name in group:
            if task in group[name]:
                group[name].remove(task)
                write_file(data)
                clearPrevOutput()
                print(f'Task "{task}" removed from "{name}"!')
            else:
                print("Task not found!")
            return
    print("Category not found!")


def main() -> None:
    while True:
        print("\nThese are the current TODO's:")
        showOutput()

        print("\nWhat you want to do...? ")
        print("\t1. Add Category")
        print("\t2. Remove Category")
        print("\t3. Add Task")
        print("\t4. Remove Task")
        print("\t5. Exit")

        choice = input("Enter choice: ").strip()
        if choice == "1":
            addCategory()
        elif choice == "2":
            removeCategory()
        elif choice == "3":
            addTask()
        elif choice == "4":
            removeTask()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    print("Welcome to Pavan's TODO List")
    main()
