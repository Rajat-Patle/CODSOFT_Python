class ToDoList:
    def __init__(self):
        self.task = []
        self.choice = 0 
    
    def add_task(self):
        self.n_task = int(input("Enter the Number of Task: "))
        for a in range(1, self.n_task + 1):
            self.li = str(input("Enter your Task: "))
            self.task.append(self.li)
            with open("Task.txt", 'a') as file:
                file.write(self.li + "\n")
        print("Your task has been added Successfully!!")
    
    def display_task(self):
        print("The Task Present are :")
        self.file = open("Task.txt",'r')
        self.c=0
        while True:
            self.line = self.file.readline().strip()
            self.c+=1
            if not self.line:
                break
            print(self.c,".",self.line)
            
    def fetch_data(self):
        fetch = open("Task.txt",'r')
        while True:
            line = fetch.readline().strip()
            if not line:
                break
            self.task.append(line)
    
    def update_task(self):
        print("\n|----- Your Scheduled Tasks -----|")
        for a in range(0,len(self.task)):
            print(f"{a+1}. {self.task[a]}")
        self.index2=int(input("\nWhich task no. you have to change or update: "))
        
        if(self.index2>len(self.task) or self.index2<0):
            print("!!!_ Please enter the valid index no. or task no. _!!!")
        else:
         self.newtask=str(input("\nWhat is your new updated task :- "))
         self.oldtask=self.task[self.index2-1]
         self.task.remove(self.oldtask)
         print(f"\n!!! Your Task {self.newtask} is under updating process !!! ")
         self.task.insert(self.index2-1,self.newtask)
         print(f"\n!!! Your Task {self.newtask} has been updated !!! ")
    
    def delete_task(self):
        for a in range(0,len(self.task)):
            print(f"{a+1}. {self.task[a]}")
        self.delete_index=int(input("\nEntre which task you want to Delete: "))
        
        if(self.delete_index > len(self.task) or self.delete_index<0):
            print("!!!_ Please enter the valid index no. or task no. _!!!")
        else:
            self.oldtask=self.task[self.delete_index-1]
            self.task.remove(self.oldtask)
            print(f"{self.oldtask}\n Has been Deleted Successfully!")


            
    def save_task(self):
       print("\n!!! Your all tasks has been under saving process !!!")
       file1=open("Task.txt",'w')
       file1.write("")
       file1.close()
       file=open("Task.txt",'a')
       for a in range(0,len(self.task)):
          file.write(self.task[a])
          file.write("\n")

       print("\n!!! Your all Tasks has been saved Succesfully !!!") 
       file.close()

    
    def menu(self):
        while(self.choice!=5):
            print("\n|===== TO-DO LIST MENU =====|")
            print("\n1.Add Tasks\n2.Show Task\n3.Update Task\n4.Delete Task\n5.Save and Exit")
            self.choice=int(input("\nEnter your Choice (1 to 5) :- "))
            
            match(self.choice):
                case 1:
                    self.add_task()
                case 2:
                    self.display_task()
                case 3:
                    self.update_task()
                case 4:
                    self.delete_task()
                case 5:
                    self.save_task()
                    
T = ToDoList()
T.fetch_data()
T.menu()