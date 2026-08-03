import string
import sys


# Task: Represents a task.
#
# description: Description of the task.
# id: The id number of the task.
class Task:

    def __init__(self, description, id):
        self.description = description
        self.id = id

# TaskList: Represents the list of tasks.
#
# items: Array of tasks.
class TaskList:

    def __init__(self):
        self.items = []




# User can add, delete, and view items in a to-do list.
def main():
    print("Hello world!")

    taskList = TaskList()
    newTaskId = 1

    keepGoing = True
    option: int # 1 = view list 
                # 2 = add new task
                # 3 = delete a task

    while keepGoing:
        print("********************\n")
        print("> Options:\n")
        print("[0] Exit program\n")
        print("[1] View to-do list\n")
        print("[2] Add new task")
        print("[3] Delete a task\n")
        print("********************\n")
        print("\n")

        option = input("Select an option: ")

        match option:

            # Exit program
            case 0:
                print("Exiting program...")
                sys.exit(0)

            # Print task list
            case 1:
                print("* TASK LIST: *\n")

                for item in taskList:
                    print(f"[{item.id}] {item.description}")

            # Add a new task
            case 2:
                newTaskDescription = input("New task description: ")
                newTask = Task(newTaskDescription, newTaskId)
                newTaskId += 1
                taskList.add(newTask)

            # Delete a task
            case 3:
                print("Which task to delete?\n")
                taskIdToDelete = input("Enter task ID: ")

                taskRemoved = False
                for task in taskList:
                    if task.id == taskIdToDelete:
                        taskList.remove(task)
                        print(f"Task: \"{task.description}\" removed from list.")
                        taskRemoved = True

                if not taskRemoved:
                    print(f"No task with ID {taskIdToDelete} found.\n")


                







if __name__ == "__main__":
    main()