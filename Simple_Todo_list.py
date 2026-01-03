from datetime import datetime

def enterTime(start:bool):
    if start == True:
        print("Enter the start date")
    else:
        print("Enter the end date")
    month = input("Enter the month in format (MM): ")
    day = input("Enter the day in format (DD): ")
    hour = input("Enter the hour in foramt (HH): ")
    min = input("Enter the minute in format (MM): ")
    return f"{month}-{day}|{hour}:{min}"

class Task:
    #Add new task--------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        self.title = input('Enter the task title: ')
        self.start_time:str = enterTime(True)
        self.end_time = enterTime(False)
        self.completed:bool = False

    #Edit task information-----------------------------------------------------------------------------------------------------------
    def editTask(self):
        print("1.Edit title \n2.Edit start time \n3.Edit end time")
        choice:int = int(input())
        match(choice):
            case 1:
                self.title = input('Enter the new title: ')
            case 2:
                self.start_time = enterTime(True)
            case 3:
                self.end_time = enterTime(False)

    #print task information----------------------------------------------------------------------------------------------------------
    def showTask(self):
        if self.completed == True:
            status = 'Completed'
        else:
            status = 'Ongoing'
        return f"{self.title} | start time[{self.start_time}] | end time[{self.end_time}] | Status: {status}"

#main func---------------------------------------------------------------------------------------------------------------------------
def main():
    tasks = []
    is_running = True

    while(is_running):
        print('Tasks list:')
        for n in range(len(tasks)):
            print(f"{n+1}.{tasks[n].showTask()}")

        print("A.Add task \nD.Edit task \nR.Remove task \nC.complete a task \nE.Exit")
        choice = input().lower()

        if choice == 'e':
            is_running = False
            continue

        match(choice):
            case 'a':
                tasks.append(Task())
            case 'd':
                sel_task:int = int(input("Enter the number of the task you want to edit: ")) - 1
                tasks[sel_task].editTask()
            case 'r':
                sel_task:int = int(input("Enter the number of the task you want to edit: ")) - 1
                tasks.pop(sel_task)
            case 'c':
                sel_task:int = int(input("Enter the number of the task you want to edit: ")) - 1
                tasks[sel_task].completed = True


if __name__ == '__main__':
    main()