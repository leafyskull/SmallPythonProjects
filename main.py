import string


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

    taskList = []

    keepGoing = True
    option: int # 1 = view list 
                # 2 = add new task
                # 3 = delete a task

    while keepGoing:
        print("********************\n")
        print("> Options:\n")
        print("[1] View to-do list\n")
        print("[2] Add new task")
        print("[3] Delete a task\n")
        print("********************\n")
        print("\n")

        option = input("Select an option: ")

        match option:
            # Print task list
            case 1:
                print("* TASK LIST: *\n")

                for item in taskList:








if __name__ == "__main__":
    main()