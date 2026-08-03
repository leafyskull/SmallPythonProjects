import string


# Task: Represents a task.
#
# description: Description of the task.
class Task:

    def __init__(self, description):
        self.description = description

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

    while keepGoing:
        print("********************\n")
        print("> Options:\n")
        print("[1] View to-do list\n")
        print("[2] Add new task")
        print("[3] Delete a task\n")
        print("********************\n")







if __name__ == "__main__":
    main()