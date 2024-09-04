# to-do list

tasks = []
checked_off_tasks = []


def task_modifier():
    option = input("Select an option: [a] - Add Task | [b] - Remove/Check off Task | [c] - Edit Task | [d] - Undo Task").lower()

    if option == 'a':
        input_task = input("Enter Task Name: ")
        tasks.append(input_task)
        print(f"Added task: '{input_task}' ! ")
        return input_task

    if option == 'b':
        which_task = input("Enter name of task you'd like to check off (Case Sensitive): ")
        if which_task in tasks:
            tasks.remove(which_task)
            checked_off_tasks.append(which_task)
            print(f"Task: '{which_task}' has been checked off! Yay!")
            return which_task
        else:
            print("Task not found. This program is case-sensitive, try again.")

    if option == 'c':
        current_task = input("Enter the title of the task you'd like to edit (Case Sensitive): ")
        if current_task in tasks:
            new_task = input("Enter the new title of the task: ")
            index = tasks.index(current_task)
            tasks[index] = new_task
            print(f"'{current_task}' has been changed to '{new_task}'.")
        else:
            print("Task not found. This program is case-sensitive, try again.")


    if option == 'd':
        select_option = input("Select an option: [a] - Undo Check (Brings task back to task-list)").lower()
        if select_option == 'a':
            name_of_task = input("Enter name of task (Case Sensitive)")
            if name_of_task in checked_off_tasks:
                index = checked_off_tasks.index(name_of_task)
                undone_task = checked_off_tasks.pop(index)
                tasks.append(undone_task)
                print(f"{name_of_task} has been undone and added back to the task list.")
            else:
                print("Task not found, This program is case-sensitive, try again.")

    else:
        print("Invalid input. Please input a correct option [a/b/c]")


def list_tasks():
    if tasks:
        print("Here are your tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    elif checked_off_tasks:
        print("Checked-off tasks:")
        for index, task in enumerate(checked_off_tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("You have no tasks added yet.")


def main():
    while True:
        menu = print("""Welcome to the To-Do List menu! Select from one of the options below:

        [1] Add/Modify Task
        [2] List out tasks
        [3] Quit
        """)

        menu_option = int(input("Enter in your choice: [1/2/3] "))

        if menu_option == 1:
            task_modifier()

        elif menu_option == 2:
            list_tasks()

        elif menu_option == 3:
            print("Quitting program. Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()


