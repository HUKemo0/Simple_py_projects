from datetime import datetime as dt

class Tasks:
  def __init__(self):
    self.title:str = input("Enter the task title: ")
    self.status:str = "In progress"
    self.start_time = f"{dt.now().month}-{dt.now().day}/{dt.now().hour}:{dt.now().second}"
  

def main():
  tasks_list = []
  completee_tasks = []
  is_running:bool = True


  while(is_running):
    print("""1.Show all tasks
2.Add tasks
3.Edit task title
4.Check task as completeb/incompleted
5.Delete task
6.Exit""")
    choice:int = int(input("Enter your choice (1-6): "))

    if choice == 6:
      break

    elif choice == 2:
      tasks_list.append(Tasks())

    elif choice == 1:
      for task in tasks_list:
        counter:int = 1
        print(f"{counter}.{task.title} - {task.status} ({task.start_time})")
        counter += 1
      else:
        print('=' * 40)

    elif choice == 3:
      task_choice = int(input("Enter the task you want to edit: "))
      tasks_list[task_choice - 1].title = input("Enter the new title: ")

    elif choice == 4:
      task_choice = int(input("Enter the task you want to edit: "))
      if tasks_list[task_choice - 1].status == 'In progress':
        tasks_list[task_choice - 1].status = 'Completed'
      else:
        tasks_list[task_choice - 1].status = 'In progress'

    elif choice == 5:
      task_choice = int(input("Enter the task you want to edit: "))
      tasks_list.pop(task_choice - 1)



if __name__ == '__main__':
  main()