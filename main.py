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

    taskList = TaskList()
    newTaskId = 1

    keepGoing = True
    option: int # 1 = view list 
                # 2 = add new task
                # 3 = delete a task

    while keepGoing:
        print("********************")
        print("> Options:")
        print("[0] Exit program")
        print("[1] View to-do list")
        print("[2] Add new task")
        print("[3] Delete a task")
        print("********************")
        print("\n")

        option = input("Select an option: ")

        match option:

            # Exit program
            case "0":
                print("Exiting program...")
                sys.exit(0)

            # Print task list
            case "1":
                print("* TASK LIST: *")

                for item in taskList.items:
                    print(f"[{item.id}] {item.description}")

                enterToContinue()

            # Add a new task
            case "2":
                newTaskDescription = input("New task description: ")
                newTask = Task(newTaskDescription, newTaskId)
                newTaskId += 1
                taskList.items.append(newTask)

                enterToContinue()

            # Delete a task
            case "3":
                print("Which task to delete?")
                taskIdToDelete = input("Enter task ID: ")

                taskRemoved = False

                for task in taskList.items:
                    if str(task.id) == taskIdToDelete:
                        taskList.items.remove(task)
                        print(f"Task: \"{task.description}\" removed from list.")
                        taskRemoved = True
                        enterToContinue()

                if not taskRemoved:
                    print(f"No task with ID {taskIdToDelete} found.\n")
                    enterToContinue()


                
def enterToContinue():
    input("Press enter to continue...")






if __name__ == "__main__":
    main()