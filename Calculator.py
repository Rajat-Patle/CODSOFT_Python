class Calculator:
          def __init__(self):
                    self.num1 = 0
                    self.num2 = 0
                    self.choice = 0
          def Input(self):
                    self.num1 = int(input("Entre the 1st Number :"))
                    self.num2 = int(input("Entre the 2nd Number :"))
                    print("First number is :",self.num1,"\nSecond number is",self.num2)
          
          def Addition(self):
                    self.sum = self.num1+self.num2
                    print("Addition :",self.sum)
          
          def Division(self):
                    self.div = self.num1//self.num2
                    print("Division :",self.div)
          
          def Multiplaction(self):
                    self.mul = self.num1*self.num2
                    print("Multiplaction :",self.mul)
          
          def Substraction(self):
                    self.sub = self.num1-self.num2
                    print("Substraction :",self.sub)

          def menu(self):
                    while(self.choice<5):
                              print("Enter the Operation you want to perform:-\n1.Addition\n2.Substraction\n3.Division\n4.Multiplaction\n5.Exit\n")
                              self.choice = int(input("Entre your choice :"))
                              match(self.choice):
                                        case 1:
                                                  self.Input()
                                                  self.Addition()
                                        case 2:
                                                  self.Input()
                                                  self.Substraction()
                                        case 3:
                                                  self.Input()
                                                  self.Division()
                                        case 4:
                                                  self.Input()
                                                  self.Multiplaction()
                                        case 5:
                                                  print("You have been Exited Successfully!!")
                                                  break
                                        case _:
                                                  print("Invalid Choice! Please entre the valid choice!")
C = Calculator()
C.menu()