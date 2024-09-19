import os
import random
import time
Person_Data = []

def Welcome_Page():
  print("---------------------------------------------")
  print("\t\tWelcome to RConsole Bank")
  print("\t\t1. Create Account")
  print("\t\t2. Login")
  print("\t\t3. Costumer Services")
  print("\t\t4. Exit")
  print("---------------------------------------------")
  choice = int(input("\tEnter your choices: "))
  if (choice == 1):
    Create_Account()
  elif (choice == 2):
    Login()
  elif (choice == 3):
    Costumer_Services()
  elif (choice == 4):
    print("\t\tThank you for using BO Banking Online")
  else:
    print("\t\tInvalid Input")

#Create Account
def Create_Account():
    os.system('clear')
    print("----------------------------")
    print("\t\tCreate Account")
    print("----------------------------")
    firstname = input("\tFirst name: ")
    middlename = input("\tMiddle name: ")
    lastname = input("\tLast name: ")
    birthdate = input("\tBirthdate(mm/dd/yy): ")
    email = input("\tEmail: ")
    address = input("\tAddress: ")
    password = input("\tPassword: ")
    Person_info = {
        "First Name": firstname,
        "Middle Name": middlename,
        "Last Name": lastname,
        "Birthdate": birthdate,
        "Email": email,
        "Address": address,
        "Password": password,
        "Balance": 0
    }
    os.system('clear')
    print("----------------------------")
    print("\t\tPlease Check all the information if it is correct")
    print("\tFirst Name: ", firstname)
    print("\tMiddle Name: ", middlename)
    print("\tLast Name: ", lastname)
    print("\tBirthdate: ", birthdate)
    print("\tEmail: ", email)
    print("\tAddress: ", address)
    print("----------------------------")
    choice = input("\tIs this information correct? (y/n): ")
    if choice.lower() == "y":
        os.system('clear')
        Random = random.randint(0,9999)
        Person_info["Account Number"] = str(Random)
        Person_Data.append(Person_info)
        print("\t\tAccount created successfully. Your Account Number is ", Person_info["Account Number"])
        Welcome_Page()
    elif choice.lower() == "n":
        print("\t\tAccount creation canceled.")
        Welcome_Page()
    else:
      print("Input Failed, returning to home page")
      
  
    

#Successfully Log in
def Success(Log_Number):
  os.system("clear")
  for Person_info in Person_Data:
    if Log_Number == Person_info["Account Number"]:
       print("\t\tHello ", Person_info["First Name"])
  print("---------------------------------------------")
  print("\t1. Show Balance")
  print("\t2. Deposit")
  print("\t3. Withdraw")
  print("\t4. Send Money")
  print("\t5. Account Information")
  print("\t6. Exit and Log out")
  print("---------------------------------------------")
  choice = int(input("Enter choices: "))
  if choice == 1:
    Show_Balance(Log_Number)
  elif choice == 2:
    Deposit(Log_Number)
  elif choice == 3:
    Withdraw(Log_Number)
  elif choice == 4:
    Send_Money(Log_Number)
  elif choice == 5:
    Account_Information(Log_Number)
  elif choice == 6:
    Welcome_Page()
  else:
    print("Error")
    
  
def Show_Balance(Log_Number):
  for Person_info in Person_Data:
    if Log_Number == Person_info["Account Number"]:
      print("Your Balance is", Person_info["Balance"])
      Success(Log_Number)
def Deposit(Log_Number):
  for Person_info in Person_Data:
    if Log_Number == Person_info["Account Number"]:
      Deposit = float(input("Enter ammount youb want to deposit: "))
      Person_info["Balance"] = Person_info["Balance"] + Deposit
      print("Updated Balance: ", Person_info["Balance"])
      Success(Log_Number)
  
def Withdraw(Log_Number):
  for Person_info in Person_Data:
    if Log_Number == Person_info["Account Number"]:
      Withdraw = float(input("Enter ammount you want to withdraw: "))
      if Person_info["Balance"] < Withdraw:
        print("Not enough Balance")
        print("Your Balance is ", Person_info["Balance"])
        Success(Log_Number)
      elif Person_info["Balance"] > Withdraw:
        Person_info["Balance"] = Person_info["Balance"] - Withdraw
        Success(Log_Number)
        
def Send_Money(Log_Number):
  for Person_info in Person_Data:
    if Log_Number == Person_info["Account Number"]:
      Account_Transfer = input("Enter account number you want to send a money: ")
      Send_Money = float(input("Enter Ammount: "))
      Person_info["Balance"] = Person_info["Balance"] - Send_Money
      for Person_info in Person_Data:
        if Account_Transfer == Person_info["Account Number"]:
          Person_info["Balance"] = Person_info["Balance"] + Send_Money
          print("Transfer Success")
          Success(Log_Number)


def Account_Information(Log_Number):
  os.system('clear')
  for Person_info in Person_Data:
    if Log_Number == Person_info["Account Number"]:
      print("----------------------------")
      print("\t\tACCOUNT INFORMATION")
      print("\tFirst Name: ", Person_info["First Name"])
      print("\tMiddle Name: ", Person_info["Middle Name"])
      print("\tLast Name: ", Person_info["Last Name"])
      print("\tBirthdate: ", Person_info["Birthdate"])
      print("\tEmail: ", Person_info["Email"])
      print("\tAddress: ", Person_info["Address"])
      print("----------------------------")

      choice = input("Press (b) to go back: ")
      if(choice == "b"):
        Success(Log_Number)
  
#Costumer Services
def Costumer_Services():
  os.system('clear')
  print("Not available at this moment")
  time.sleep(2)
  Welcome_Page()
  
def Exit():
  os.system('clear')


#Login
def Login():
  os.system('clear')
  print("---------------------------------------------")

  print("\t\t\t\tLogin")
  print("---------------------------------------------")

  Log_Number = input("Enter your Account Number: ")
  Log_Password = input("Enter your Password: ")
  for Person_info in Person_Data:
    if (Log_Number == Person_info["Account Number"] and Log_Password == Person_info["Password"]):
       Success(Log_Number)
    else:
      print("Error")
      Welcome_Page()


Welcome_Page()