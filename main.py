# create  new task
# we will store the tasks in a list
# we could delete some tasks
# we could modify some tasks
# view tasks
# Quit

options = ["1- add new task", "2- Mark task as complete", "3- view tasks", "4- Quit"]
tasks = []


def add_New_Task():
    # get task fro user
    task = input("Enter your task :  ")
    # Infos about task
    task_info = {'task': task, 'completed': False}
    # add the task in the list of tasks
    tasks.append(task_info)
    print("Task added to the list ")


# mark as completed function
def mark_As_Complete():
    # get list of incompleted tasks
    incompleted_Tasks = [task for task in tasks if task["completed"] is False]

    # show tasks to the user
    for incompleted_Task in incompleted_Tasks:
        print(incompleted_Task['task'])
        print("-" * 30)
    # get the task from the user
    completed_Task = input("Enter the task you completed : ")

    completed_Task = input("Enter the completed task : ")
    tasks.remove(completed_Task)


def view_Tasks():
    for task in tasks:
        print(task)


while True:
    for option in options:
        print(option)

    choice = input("Enter Your choice :")
    if choice == "1":
        add_New_Task()
    elif choice == "2":
        mark_As_Complete()
    elif choice == "3":
        view_Tasks()
    elif choice == "4":
        break
    else:
        print("Invalid option please try again")




