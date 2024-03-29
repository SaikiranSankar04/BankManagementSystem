import mysql.connector as M 
import random 
from prettytable import PrettyTable 
mydb = M.connect (host = "localhost", user = "root", password = "", database = "SCHOOL") 
mycur = mydb.cursor () 
a = 0 
 
def Display_Table1 ():
    global a 
    mycur.execute ("SELECT * FROM PERSONALDETAILS") 
    k = mycur.fetchall () 
    mytable =PrettyTable (["ACC NO.", "NAME", "AGE", "RESIDENTIAL ADDRESS","E-MAIL ADDRESS", "PHONE NUMBER"]) 
    for i in k:
        if i[0] == a: 
            mytable.add_row ([i[0], i[1], i[2], i[3], i[4], i[5]]) 
            return mytable 
    
def Display_Table2 ():
    global a 
    mycur.execute ("SELECT * FROM CUSTOMERACCOUNT") 
    k = mycur.fetchall () 
    mytable = PrettyTable (["ACCOUNT NUMBER", "NAME", "CURRENT ACCOUNT", "SAVINGS ACCOUNT","FIXED DEPOSITS"]) 
    for i in k:
        if i [0] == a: 
            mytable.add_row ([i[0], i[1], i[2], i[3], i[4]]) 
            return mytable 
    
def Display_Table3 ():
    global a 
    mycur.execute ("SELECT * FROM LOANDETAILS") 
    r = mycur.fetchall () 
    mytable = PrettyTable (["ACCOUNT NUMBER", "NAME", "PERSONALLOAN", "HOMELOAN", "AUTOLOAN","MORTGAGE"]) 
    for i in r:
        if i[0] == a: 
            mytable.add_row ([i[0], i[1], i[2], i[3], i[4], i[5]]) 
            return mytable 
 
def accnocheck ():
    global a 
    t = (a,) 
    mycur.execute ("SELECT * FROM ACCNOS") 
    k = mycur.fetchall () 
    c = 0 
    while t not in k:
        print ("INVALID INPUT") 
        c += 1 
        if c<2:
            a = int (input ("Enter a valid account number:")) 
            t = (a,) 
        else:
            print ("Press 1 to try again or 2 to return to the home screen") 
            ch = int (input ("Enter a choice:")) 
            if ch == 1:
                a = int (input ("Enter a valid account number:")) 
                t = (a,) 
            else: 
                choosemode () 
    
def Create ():
    global a 
    while True:
      print ("Enter the following details:")
      n = input ("Name:") 
      age = int (input ("Age:")) 
      if age < 18:
        print ("You are not eligible to create an account")
        break 
      r = input ("Residential Address:") 
      e = input ("E-mail Address:") 
      p = int (input ("Phone Number:")) 
      a = random.randint (1000000, 9999999) 
      mycur.execute ("SELECT * FROM ACCNOS") 
      k = mycur.fetchall () 
      while True:
        mycur.execute ("SELECT * FROM ACCNOS") 
        k = mycur.fetchall () 
        t = (a,) 
        if a not in k:
          mycur.execute (("INSERT INTO ACCNOS VALUES(%s)"), t) 
          break 
        else:
          a = random.randint (1000000, 9999999)
          d="INSERT INTO PERSONALDETAILS VALUES(%s,%s,%s,%s,%s,%s)"
          mycur.execute (d, (a, n, age, r, e, p)) 
          print ("Your account has been created successfully!") 
          print ("Your account details are as follows:") 
          print (Display_Table1 ()) 
          print ("Now, create a minimum deposit for your account;") 
          am = int (input ("Enter the amount you would like to deposit:")) 
          if 10000 > am:
            print ("The minimum deposit required is Rs.10000")
            am = int (input ("Enter a valid amount to deposit:")) 
            v = "INSERT INTO CUSTOMERACCOUNT (ACCNO,NAME,CURRENTACCOUNT) VALUES(%s,%s,%s)" 
            mycur.execute (v, (a, n, am)) 
            print ("Deposition successful!!!") 
            print () 
            w = "INSERT INTO LOANDETAILS (ACCNO,NAME) VALUES(%s,%s)" 
            mycur.execute (w, (a, n)) 
            break 
    
def Modify ():
  print (''' ***MODIFY MENU***
  WHICH OF THE FOLLOWING WOULD YOU LIKE TO MODIFY?
  1. Modify Name
  2. Modify Age
  3. Modify Residential Address
  4. Modify E-mail Address
  5. Modify Phone Number
  Else press 6 to return to the main menu ''') 
  choice = int (input ("Enter a choice from the MODIFY Menu:")) 
  global a 
  while True:
    if choice == 1:
      a = int (input ("Enter account number:")) 
      accnocheck () 
      n = input ("New Name:") 
      mycur.execute (("UPDATE PERSONALDETAILS SET NAME=%s WHERE ACCNO=%s"), (n, a)) 
      print ("Updated account details are as follows:") 
      print (Display_Table1 ()) 
    elif choice == 2:
      a = int (input ("Enter account number:")) 
      accnocheck () 
      ag = int (input ("New Age:")) 
      mycur.execute (("UPDATE PERSONALDETAILS SET AGE=%s WHERE ACCNO=%s"),(ag, a)) 
      print ("Updated account details are as follows:") 
      print (Display_Table1 ()) 
    elif choice == 3:
      a = int (input ("Enter account number:")) 
      accnocheck () 
      r = input ("New Residential Address:") 
      mycur.execute (("UPDATE PERSONALDETAILS SET RESIDENTIALADDRESS=%s WHERE ACCNO=%s"), (r, a)) 
      print ("Updated account details are as follows:") 
      print (Display_Table1 ()) 
    elif choice == 4:
      a = int (input ("Enter account number:")) 
      accnocheck () 
      e = input ("New E-mail Address:") 
      mycur.execute (("UPDATE PERSONALDETAILS SET EADD=%s WHERE ACCNO=%s"), (e, a)) 
      print ("Updated account details are as follows:") 
      print (Display_Table1 ()) 
    elif choice == 5:
      a = int (input ("Enter account number:")) 
      accnocheck () 
      p = int (input ("New Phone Number:")) 
      mycur. execute (("UPDATE PERSONALDETAILS SET PHNO=%s WHERE ACCNO=%s"), (p, a)) 
      print ("Updated account details are as follows:") 
      print (Display_Table1 ()) 
    elif choice == 6:
      print ("Exiting") 
      break 
    else:
      print ("INVALID INPUT: ENTER A CHOICE ONLY BETWEEN 1 TO 6") 
      choice = int (input ("Enter a choice from the MODIFY Menu:")) 
    
def Withdraw ():
  global a 
  a = int (input ("Enter account number:")) 
  accnocheck () 
  s = int (input ("Enter amount you would like to withdraw:")) 
  mycur.execute ("SELECT * FROM CUSTOMERACCOUNT") 
  k = mycur.fetchall () 
  for i in k:
    if i[0] == a:
      d = i[2] 
  amt = d - s 
  if s>d:
    print ("Current balance is", d,"\nThe value entered is more than current balance!") 
    print ("Would you like to try again? Press 1 to try again or 2 to return to the main menu;")
    while True:
      ch = int (input ("Enter your choice:")) 
      if ch == 1:
        Withdraw ()
        break 
      elif ch == 2:
        adminmainmenu() 
        break 
      else: 
        print ("Invalid choice:") 
  elif amt < 10000:
    print ("Withdrawal leads to insuffiecient minimum balance") 
    print("Would you like to try again? Press 1 to try again or 2 to return to the main menu;") 
    while True:
      ch = int (input ("Enter your choice:")) 
      if ch == 1:
        Withdraw () 
        break 
      elif ch == 2:
        adminmainmenu () 
        break 
      else:
        print ("Invalid choice:") 
  else: 
    m = "UPDATE CUSTOMERACCOUNT SET CURRENTACCOUNT=%s WHERE ACCNO=%s" 
    mycur.execute (m, (amt, a)) 
    Display_Table2 () 
    print ("Rs.", s, "has been withdrawn from your account with account number:", a, "\nAmount remaining in your account is Rs.", amt) 

def Deposit ():
  global a 
  a = int (input ("Enter your account number:")) 
  accnocheck () 
  print (''' ***DEPOSIT MENU***
  DEPOSIT AMOUNT IN:
  1.Current Account
  2.Savings Account
  3.Fixed Deposit
  4.Exit''') 
  ch = int (input ("Enter a choice from the DEPOSIT Menu:")) 
  while True:
    if ch == 1:
      Currentacc () 
    elif ch == 2: 
      Savingsacc () 
    elif ch == 3: 
      Fixeddeposit () 
    elif ch == 4:
      print ("RETURNING TO THE ADMIN MENU") 
      print () 
      adminmainmenu () 
      break 
    else:
      print ("Invalid Input") 
      ch = int (input ("Enter a choice from the DEPOSIT Menu:")) 

def Currentacc ():
  global a 
  a = int (input ("Enter your account number:")) 
  accnocheck () 
  amt = int (input ("Enter the amount you would like to deposit :")) 
  mycur.execute (("UPDATE CUSTOMERACCOUNT SET CURRENTACCOUNT=CURRENTACCOUNT+%s WHERE ACCNO=%s"), (amt, a)) 
  print ("Deposition successful!") 
  print () 
  print (Display_Table2 ()) 

def Savingsacc ():
  global a 
  a= int (input ("Enter account number:")) 
  accnocheck () 
  t = (a,) 
  mycur.execute (("SELECT SAVINGSACCOUNT FROM CUSTOMERACCOUNT WHERE ACCNO=%s"), t) 
  k = mycur.fetchall () 
  for i in k:
    if i[0] == None:
      p = int (input ("Enter principal amount:")) 
      n = emicalc (p, r = 3.5, t = 1) 
      print ("Creating a savings account with annual interest rate 3.5%;") 
      print ("Amount in your savings account after a year will be Rs.", n[1]) 
      mycur.execute (("UPDATE CUSTOMERACCOUNT SET SAVINGSACCOUNT=%s WHERE ACCNO=%s"),((n[1]), a)) 
      Display_Table2 () 
      mydb.commit () 
    else: 
      print ("Savings account with account number", a, "already exists!") 
      print (Display_Table2 ()) 

def Fixeddeposit ():
  global a 
  a = int (input ("Enter account number:")) 
  accnocheck () 
  t = (a,) 
  mycur.execute (("SELECT FIXEDDEPOSITS FROM CUSTOMERACCOUNT WHERE ACCNO=%s"),t) 
  k = mycur.fetchall () 
  for i in k:
    if i[0] == None:
      pr = int (input ("Enter principal amount:")) 
      time = int (input ("Enter number of years:")) 
      n = emicalc (p = pr, r = 4.5, t = time) 
      print ("Creating a fixed deposit with annual interest rate 4.5%;") 
      print ("Amount in your fixed deposit after", time, "year(s) will be Rs.", n[1]) 
      mycur.execute (("UPDATE CUSTOMERACCOUNT SET FIXEDDEPOSITS=%s WHERE ACCNO=%s"), ((n[1]), a)) 
      Display_Table2 () 
      mydb.commit () 
    else: 
      print ("Fixed deposit with account number", a, "already exists!") 
      print (Display_Table2 ()) 

def View ():
  global a 
  print ('''***VIEW MENU***
WHICH OF THE FOLLOWING DETAILS WOULD YOU LIKE TO VIEW?
1. YOUR PERSONAL DETAILS
2. AMOUNTS IN DIFFERENT ACCOUNTS
3. LOANS (if any)''') 
  print ("Else press 4 to return to the MAIN MENU") 
  a = int (input ("Enter your account number:")) 
  accnocheck () 
  while True:
    ch = int (input ("Enter a choice:"))  
    if ch == 1: 
      print (Display_Table1 ()) 
    elif ch == 2: 
      print (Display_Table2 ()) 
    elif ch == 3: 
      print (Display_Table3 ()) 
    elif ch == 4:
      mainmenu() 
      break
    else: 
      print ("INVALID CHOICE! ENTER A CHOICE ONLY BETWEEN 1 TO 4") 

def Viewall ():
  mytable1 = PrettyTable (["ACC NO.", "NAME", "AGE", "RESIDENTIAL ADDRESS","E-MAIL ADDRESS","PHONE NUMBER"]) 
  mycur.execute ("SELECT * FROM PERSONALDETAILS") 
  k = mycur.fetchall () 
  for i in k:
    mytable1.add_row ([i[0], i[1], i[2], i[3], i[4], i[5]]) 
    print (mytable1) 
    mycur.execute ("SELECT * FROM CUSTOMERACCOUNT") 
    k = mycur.fetchall () 
    mytable2 = PrettyTable (["ACCOUNT NUMBER", "NAME", "CURRENT ACCOUNT","SAVINGS ACCOUNT", "FIXED DEPOSITS"]) 
  for i in k:
    mytable2.add_row ([i[0], i[1], i[2], i[3],i[4]]) 
    print (mytable2) 
    mycur.execute ("SELECT * FROM LOANDETAILS") 
    k = mycur.fetchall () 
    mytable3 = PrettyTable (["ACCOUNT NUMBER", "NAME", "PERSONALLOAN","HOMELOAN", "AUTOLOAN", "MORTGAGE"]) 
  for i in k: 
    mytable3.add_row ([i[0], i[1], i[2], i[3], i[4], i[5]]) 
    print (mytable3) 

def Apply_loan ():
  global a 
  a = int (input ("Enter your account number:")) 
  accnocheck () 
  print (''' ***LOAN MENU***
  TYPES OF LOANS WE OFFER:
  1. PERSONAL LOAN
  2. HOME LOAN
  3. AUTO LOAN
  4. MORTGAGE''') 
  print ("Or press 5 to return to the MAIN Menu") 
  choice =int (input ("Enter your choice from the LOAN Menu:")) 
  while True:
    if choice == 1: 
      return personal_loan () 
    elif choice == 2: 
      return home_loan () 
    elif choice == 3: 
      return auto_loan () 
    elif choice == 4: 
      return mortgage () 
    elif choice == 5:
      print ("Exiting") 
      break
    else: 
      print ("INVALID INPUT: ENTER A CHOICE ONLY BETWEEN 1 TO 5") 

def emicalc (p, r, t): 
  mr = r / 1200 
  mo = 12 * t 
  emi = round (p * mr * ((1 + mr) ** mo) / ((1 + mr) ** mo - 1), 3) 
  temi = round ((mo * emi), 3) 
  return (emi, temi) 

def personal_loan ():
  global a
  print ("Avail personal loans at the rate of 10.5% per annum") 
  print ("Tenure: 1 to 5 years") 
  a = int (input ("Enter account number:")) 
  accnocheck () 
  mycur.execute ("SELECT * FROM LOANDETAILS") 
  k = mycur.fetchall () 
  for i in k:
    if i[0] == a:
      d = i[2] 
  if d== None:
    p = int (input ("Enter the loan amount:")) 
    time = int (input ("Enter your time period (in years):")) 
  if not 1 <= time <= 5:
    print ("INVALID INPUT") 
    time =int (input ("Enter your time period (only between 1 to 5 years):")) 
    n= emicalc (p, r = 10.5, t = time) 
    m = "UPDATE LOANDETAILS SET PERSONALLOAN=%s WHERE ACCNO=%s" 
    mycur.execute (m,(str(n[1]),a))
    mydb.commit () 
    print ("You have successfully applied for a personal loan") 
    print (Display_Table3 ()) 
    print ("Amount to be paid per month Rs.",n[0]) 
    print ("Total amount payable Rs.", n[1]) 
  else: 
    print ("Personal loan already exists") 
    print (Display_Table3 ()) 

def home_loan ():
  print ("Avail home loans at the rate of 7.2% per annum") 
  print ("Tenure: Upto 30 years") 
  a = int (input ("Enter account number:")) 
  accnocheck () 
  mycur.execute ("SELECT * FROM LOANDETAILS") 
  k = mycur.fetchall () 
  for i in k:
    if i[0] == a: 
      d = i[3] 
  if d== None:
    p = int (input ("Enter the loan amount:")) 
    time = int (input ("Enter your time period (in years):")) 
    if not 1 <= time <= 30:
      print ("INVALID INPUT")  
      time =int (input ("Enter your time period (only between 1 to 30 years):")) 
    n = emicalc (p, r = 7.2, t = time) 
    m ="UPDATE LOANDETAILS SET HOMELOAN=%s WHERE ACCNO=%s" 
    mycur.execute (m,((str(n[1]),a)))    
    mydb.commit () 
    print ("You have successfully applied for a home loan") 
    print (Display_Table3 ()) 
    print ("Amount to be paid per month Rs.",n[0]) 
    print ("Total amount payable Rs.", n[1]) 
  else: 
    print ("Home loan already exists") 
    print (Display_Table3 ()) 

def auto_loan ():
  print ("Avail auto loans at the rate of 8% per annum") 
  print ("Tenure: 1 to 8 years") 
  a = int (input ("Enter account number:")) 
  accnocheck () 
  mycur.execute ("SELECT * FROM LOANDETAILS") 
  k = mycur.fetchall () 
  for i in k:
    if i[0] == a:
      d = i[4] 
  if d == None:
    p = int (input ("Enter the loan amount:")) 
    time = int (input ("Enter your time period (in years):")) 
    if not 1 <= time <= 8:
      print ("INVALID INPUT")  
      time =int (input ("Enter your time period (only between 1 to 8 years):")) 
    n = emicalc (p, r = 8, t = time) 
    m ="UPDATE LOANDETAILS SET AUTOLOAN=%s WHERE ACCNO=%s" 
    mycur.execute (m,((str(n[1]),a))) 
    mydb.commit () 
    print ("You have successfully applied for a auto loan") 
    print (Display_Table3 ()) 
    print ("Amount to be paid per month Rs.",n[0]) 
    print ("Total amount payable Rs.", n[1]) 
  else:
    print ("Auto loan already exists") 
    print (Display_Table3 ()) 
 
def mortgage ():
  global a 
  print ("Avail a mortgage at the rate of 9% per annum") 
  print ("Tenure: Upto 15 years") 
  a = int (input ("Enter account number:")) 
  accnocheck () 
  mycur.execute ("SELECT * FROM LOANDETAILS") 
  k = mycur.fetchall () 
  for i in k:
    if i [0] == a:
      d = i[5] 
  if d == None:
    p = int (input ("Enter the loan amount:")) 
    time = int (input ("Enter your time period (in years):")) 
    if not 1 <= time <= 9:
      print ("INVALID INPUT")
    time =int (input ("Enter your time period (only between 1 to 9 years):")) 
    n= emicalc (p, r = 9, t = time) 
    m ="UPDATE LOANDETAILS SET MORTGAGE=%s WHERE ACCNO=%s" 
    mycur.execute (m,((str(n[1]),a)))
    mydb.commit () 
    print ("You have successfully applied for a mortgage") 
    print (Display_Table3 ()) 
    print ("Amount to be paid per month Rs.",n[0]) 
    print ("Total amount payable Rs.", n[1]) 
  else: 
    print ("Mortgage already exists") 
    print (Display_Table3 ()) 

def Repay_loan ():
  global a 
  a = int (input ("Enter your account number:")) 
  accnocheck () 
  print (''' ***LOAN REPAYMENT MENU***
  REPAY:
  1.PERSONAL LOAN
  2.HOME LOAN
  3.AUTO LOAN
  4.MORTGAGE''') 
  print ("Or press 5 to return to the MAIN Menu") 
  choice = int (input ("Enter your choice from the LOAN Menu:")) 
  while True:
    if choice == 1: 
      return repay_personal_loan() 
    elif choice == 2:
      return repay_home_loan() 
    elif choice == 3:
      return repay_auto_loan() 
    elif choice == 4: 
      return repay_mortgage() 
    elif choice == 5:
      print ("Exiting") 
      break
    else: 
      print ("INVALID INPUT: ENTER A CHOICE ONLY BETWEEN 1 TO 5") 

def repay_personal_loan ():
  global a 
  a = int (input ("Account Number:")) 
  accnocheck () 
  t = (a,) 
  while True:
    mycur.execute ("SELECT * FROM LOANDETAILS") 
    k = mycur.fetchall () 
    for i in k:
      if i[0] == a:
        d = i[2]  
    if d is not None:
      amt = float (input ("Amount you are repaying:")) 
      due = float (d) - amt 
      if due > 0:
        mycur.execute (("UPDATE LOANDETAILS SET PERSONALLOAN=%s WHERE ACCNO=%s"), (due, a))
        print ("Due", due) 
        break 
      elif due == 0:
        mycur. execute (("UPDATE LOANDETAILS SET PERSONALLOAN=%s WHERE ACCNO=%s"),(None,a)) 
        print ("All loans have been cleared!") 
        break 
      else:
        print("Amount paid is greater than the due amount;\nAmount to be paid is Rs.",d) 
    else: 
      print ("You have no personal loans to be repaid") 
      print (Display_Table3 ()) 
      break 

def repay_home_loan ():
  global a 
  a = float (input ("Account Number:")) 
  accnocheck () 
  t = (a,) 
  while True:
    mycur.execute ("SELECT * FROM LOANDETAILS") 
    k = mycur.fetchall () 
    for i in k:
      if i[0] == a:
        d = i[3] 
    if d is not None:
      amt = float (input ("Amount you are repaying:")) 
      due = float (d) - amt 
      if due < 0:
        print ("Amount paid is greater than the due amount;\nAmount to be paid is Rs.", d)
      elif due == 0:
        mycur.execute (("UPDATE LOANDETAILS SET HOMELOAN=%s WHERE ACCNO=%s"),(None,a)) 
        print ("All loans have been cleared!") 
        break 
      else:
        mycur.execute (("UPDATE LOANDETAILS SET HOMELOAN=%s WHERE ACCNO=%s"),(due, a)) 
        print ("Due Rs.", due)    
        break 
    else: 
      print ("You have no home loans to be repaid") 
      print (Display_Table3 ()) 
      break 

def repay_auto_loan ():
  global a 
  a = int (input ("Account Number:")) 
  accnocheck () 
  t = (a,) 
  while True:
    mycur.execute ("SELECT * FROM LOANDETAILS") 
    k = mycur.fetchall () 
    for i in k:
      if i[0] == a:
        d = i[4] 
    if d is not None:
      amt = float (input ("Amount you are repaying:")) 
      due = float (d) - amt 
      if due < 0:
        print ("Amount paid is greater than the due amount;\nAmount to be paid is Rs.", d)
      elif due == 0:
        mycur.execute (("UPDATE LOANDETAILS SET AUTOLOAN=%s WHERE ACCNO=%s"),(None,a)) 
        print ("All loans have been cleared") 
        break 
      else:
        mycur.execute (("UPDATE LOANDETAILS SET AUTOLOAN=%s WHERE ACCNO=%s"),(due, a)) 
        print ("Due Rs.", due) 
        break 
    else: 
      print ("You have no auto loans to be repaid") 
      print (Display_Table3 ()) 
      break 

def repay_mortgage ():
  global a 
  a = int (input ("Account Number:")) 
  accnocheck () 
  t = (a,) 
  while True:
    mycur.execute ("SELECT * FROM LOANDETAILS") 
    k = mycur.fetchall () 
    for i in k:
      if i[0] == a:
        d = i[5] 
    if d is not None:
      amt = float (input ("Amount you are repaying:")) 
      due = float (d) - amt 
      if due < 0:
        print ("Amount paid is greater than the due amount;\nAmount to be paid is Rs.", d)
      elif due == 0:
        mycur.execute (("UPDATE LOANDETAILS SET MORTGAGE=%s WHERE ACCNO=%s"),(None,a)) 
        print ("All loans have been cleared") 
        break 
      else:
        mycur.execute (("UPDATE LOANDETAILS SET MORTGAGE=%s WHERE ACCNO=%s"),(amt, a)) 
        print ("Due Rs.", due) 
        break 
    else: 
      print ("You have no mortgage loans to be repaid") 
      print (Display_Table3 ()) 
      break 

def Delete ():
  a = int (input ("Account Number:")) 
  accnocheck () 
  t = (a,) 
  print ("Do you want to permanently delete your account?:") 
  c = input ("Enter Y or N to proceed:") 
  if c in "yY":
    mycur.execute (("DELETE FROM PERSONALDETAILS WHERE ACCNO=%s"), t) 
    mycur.execute (("DELETE FROM LOANDETAILS WHERE ACCNO=%s"), t) 
    mycur.execute (("DELETE FROM CUSTOMERACCOUNT WHERE ACCNO=%s"), t) 
    print ("Your account with account number", a, " has been deleted permanently") 
  elif c in "Nn":
    print ("Operation terminated")
  else:
    print ("Enter a valid choice") 
 
def mainmenu ():
  print () 
  print (''' ***MAIN MENU***
1. Create a new account
2. Modify personal details
3. View
4. Exit''') 
  while True:
    choice =int (input ("Enter your choice from the MAIN Menu:")) 
    print () 
    if choice == 1: 
      Create () 
    elif choice == 2: 
      Modify () 
    elif choice == 3: 
      View () 
    elif choice == 4:
      print ("THANKS FOR VISITING!!! HAVE A GOOD DAY") 
      print ("***") 
      print ()  
      choosemode() 
      break
    else:
      print ("INVALID INPUT: ENTER A CHOICE ONLY BETWEEN 1 TO 4") 
 
def adminpass():
  pw = "bankadmin@123" 
  while True:
    p = input ("Enter password:") 
    if pw== p:
      adminmainmenu () 
      break 
    else:
      print ("Incorrect password")
      print ("Press 1 to try again or 2 to exit") 
      ch = int (input ("Enter your choice:")) 
    if ch == 1: 
      adminpass ()
      break 
    elif ch == 2:
      print ("Exiting...") 
      choosemode () 
      break 
    else:
      print ("Invalid choice,enter either 1 or 2") 
 
def adminmainmenu ():
  print () 
  print (''' ***ADMIN MENU***
    1. Withdraw
    2. Deposit
    3. Apply for a loan
    4. Repay a loan
    5. Delete an account
    6. View
    7. Exit''') 
  while True:
    choice = int (input ("Enter your choice from the ADMIN Menu:")) 
    if choice == 1:
      Withdraw () 
    elif choice == 2:
      Deposit () 
    elif choice == 3:
        Apply_loan () 
    elif choice == 4: 
      Repay_loan () 
    elif choice == 5: 
      Delete () 
    elif choice == 6: 
      Viewall () 
    elif choice == 7:
      print ("Exiting...") 
      break
    else:
      print ("INVALID INPUT: ENTER A CHOICE ONLY BETWEEN 1 TO 7") 
 
def choosemode ():
  print (''' *****MENU*****
1. USER MODE
2. ADMIN MODE''') 
  while True:
    ch = int (input ("\nEnter your choice:")) 
    print () 
    if ch == 1:
      print (" *****WELCOME******\nThe services we offer are as follows:") 
      mainmenu () 
      break 
    elif ch == 2:
      adminpass () 
      break
    else:
      print ("Invalid choice,enter either 1 or 2") 
      ch = int (input ("Enter your choice:")) 
      print () 
  A ="CREATE TABLE PERSONALDETAILS(ACCNO INT PRIMARY KEY NOT NULL,NAME VARCHAR(25),AGE INT,RESIDENTIALADDRESS VARCHAR(60),EADD VARCHAR(30),PHNO CHAR(10))"
  mycur.execute (A) 
  B ="CREATE TABLE CUSTOMERACCOUNT(ACCNO INT PRIMARY KEY NOT NULL, NAME VARCHAR(25),CURRENTACCOUNT INT DEFAULT 0, SAVINGSACCOUNT INT ,FIXEDDEPOSITS INT)"
  mycur.execute (B) 
  C ="CREATE TABLE LOANDETAILS (ACCNO INT PRIMARY KEY NOT NULL, NAME VARCHAR(25),PERSONALLOAN VARCHAR(25),HOMELOAN VARCHAR(25),AUTOLOAN VARCHAR(25),MORTGAGE VARCHAR(25))"
  mycur.execute (C) 
  D ="CREATE TABLE ACCNOS (ACCNO INT)" 
  mycur.execute (D) 
  choosemode ()
