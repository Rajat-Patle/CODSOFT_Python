import random as r 
class Password_Generator:
          def __init__(self):
                    self.choice = 0
                    self.password = ""
          
          def basic_pwd(self):
                    self.len_pwd = int(input("Entre the Lenth of Password to Generate :"))
                    
                    if(self.len_pwd >=4):
                              self.no = (self.len_pwd//2)
                              for a in range(0,self.len_pwd):
                                        if(len(self.password)<self.no):
                                                  self.password += chr(r.randint(ord('a'), ord('z')))
                                        else:
                                                  self.password += str(r.randint(1,9))
                              print(f"Generated Basic Password of lenght {self.len_pwd} is: {self.password}\n")  
                              self.password = ""
                              
                    else:          
                              print("The Length of Password Should be Greater or Equal to 4!!\n")
                              
          def strong_pwd(self):
                    self.len_pwdS = int(input("Entre the Lenth of Password to Generate :"))
                    if(self.len_pwdS >=4):
                              for a in range(0,self.len_pwdS):
                                        if(len(self.password)<self.len_pwdS-3):
                                                  self.password += chr(r.randint(ord('a'), ord('z')))
                                        elif(len(self.password)==self.len_pwdS-2):
                                                  self.password += chr(r.randint(ord('#'), ord('&')))
                                        else:
                                                  self.password+=str(r.randint(1,9))
                              print(f"Generated Strong Password of lenght {self.len_pwdS} is: {self.password}\n")  
                              self.password = ""
                              

                    else:
                              print("The Length of Password Should be Greater or Equal to 4!!\n")  
          
          def complex_pwd(self):
                    self.len_pwdC = int(input("Entre the Length of the Password to Generate :"))
                    
                    if(self.len_pwdC >=4):          
                              for a in range(0,self.len_pwdC):
                                        if(len(self.password) < self.len_pwdC-4):
                                                  self.password +=  chr(r.randint(ord('A'), ord('Z')))
                                        elif(len(self.password)==self.len_pwdC-4):
                                                  self.password += chr(r.randint(ord('a'), ord('z')))
                                        elif(len(self.password)==self.len_pwdC-2):
                                                  self.password += chr(r.randint(ord('#'), ord('&')))
                                        else:
                                                  self.password+=str(r.randint(1,9))         
                              print(f"Generated Complex Password of lenght {self.len_pwdC} is: {self.password}\n")  
                              self.password = ""
 
                    else:
                              print("The Length of Password Should be Greater or Equal to 4!!\n")  
                              
          def menu(self):
                    while True:
                              print("Entre your Choice Which type of Password you want to Generate :-\n1. Basic Password\n2. Strong Password\n3. Complex Password\n4. Exit")
                              self.choice = int(input("Entre your Choice :"))
                              match(self.choice):
                                        case 1:
                                                  self.basic_pwd()
                                        case 2:
                                                  self.strong_pwd()
                                        case 3:
                                                  self.complex_pwd()
                                        case 4:
                                                  print("Program has been Terminated Successfully!!")
                                                  break
                                        case _:
                                                  print("Invalid Choice! Please Enter the Valid Option!!")                                                         

P = Password_Generator()
P.menu()