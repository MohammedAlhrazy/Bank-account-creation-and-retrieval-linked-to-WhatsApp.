import os
import time
import datetime
import pywhatkit
import random
from re import search

def sign_up():
      
   try:
      first_name=input("Enter your first name and be carful with white space:").lower()
      last_name=input("Enter your last name and be carful with white space:").lower()
      #checking email
      while True:
         email=input("Enter your email :")
         if len(email)==0:
            print("you did not enter anything")
         user,domain=email.split("@")
         if len(user)==0:
            print("incorrect input there is no domain name .")
         if "." not in domain:
            print("incorrect email you forget (.) ")
         if not(domain=="gmail.com"):
            print("Wrong extention!your gmail have to end with gmail.com")
         else:
            print("=="*10,"correct email!","=="*10)
            break
      #checking password
      while True:
         password=input("enter your password :")
         if len(password)<=7:
            print("the passwor should be grater than 7 numbers")
         else:
            if not(search("[a-z]",password) and search("[A-Z]",password)):
               print("the password should contain cabital and small letters.")
            else:
               if not(search("[0-9]",password)):
                     print("the password should contain numbers.")
               else:
                     if not(search("[!@#$%^&*]",password)):
                       print("the password should contain symboles.")
                     else:
                       print("=="*10,"strong password !","=="*10)
                       break
      #checking number
      while True:               
         phone_number=input("enter your phone number and that should be Yemeni number :")
         zip_code,number=phone_number.split("-")
         if zip_code!="+967":
            print("you didn't enter the zip code of your country correct.")
         else:
            if len(number)!=9 or len(number)>9:
               print("wrong number! your phone number should be 9 numbers")
            if not(number.startswith("77") or number.startswith("73") or number.startswith("78") or number.startswith("70") or number.startswith("71")):
               print("Sorrey,that is not a yemeni number ")
            else:
               print("=="*10,"correct number!","=="*10)
               print("now we are going to ask you two safety questions to help you if you forget your password.\n")
               
               safety_question1=input("What is the best thing you like?:")
               safety_question2=input("What is your nickname?:")
               print("=="*10,"you signed up seccessfully!","=="*10)
               break

      #save User_info
      User_info=open(first_name+last_name+".txt","w+")
      User_info.write(first_name+last_name+"\n")
      User_info.write(email+"\n")
      User_info.write(password+"\n")
      User_info.write(phone_number+"\n")
      User_info.write(safety_question1+"\n")
      User_info.write(safety_question2+"\n")
      User_info.close()

   except ValueError :
      print("=="*10,"error!","=="*10)
      print("incorrect input maybe you did not entered a @ in the email \n\
   or you did not entered  - between your zip code and your phone number.")
      print("try again")
      tray_again=input("Do you want to try again\n 1-yes\n 2-no:")
      if tray_again=="1":
         sign_up()
      elif tray_again=="2":
         print("i hope you will come back again.")
      else:
         print("Wrong! there is no choise like that. ")


#Sign in
def singe_in():
      try:
         first_name=input("Please enter your first name to chack if you have account and be carful with white space:").lower()  
         last_name=input("Please enter your last name to chack if you have account and be carful with white space:").lower() 
         User_info=open(first_name+last_name+".txt","r")
      except:
         print("Sorry! you do not have account in our Bank ,so you have to creat account.")
         creat_account=input("Do yuo want to creat account \n 1-yes\n 2-no:")
         if creat_account=="1":
            sign_up()
         elif creat_account=="2":
            exit("so sorry if you do not like our servece.i hope that you will come back again.")
         else:
            print("thre is no choice like that, the program will exit.")
            exit()

      try:
        while True:

         User_info.seek()               
         stored_first_name_and_last_name,stored_email,stored_password,stored_phone_number,stored_saftey_question1,stored_saftey_question2=User_info.read().splitlines()     
         print("You have to enter the information of your account to sign in.")
         while True:
            max_trying=4
            check_email=input("Enter your email:")
            check_password=input("Enter your password:")
            if not(check_email==stored_email and check_password==stored_password):
               if not(check_email==stored_email):
                  print("Your email is not correct.")
               else:
                  print("Your password is not correct.")
               max_trying-=1
               print(f"Wrong information You stail have {max_trying} trying")
               if max_trying<=0:
                  print("Lots of wrong attempts.You blocked for 1 hour")
                  time.sleep(3600)
                  print("the block is open.")
                  if_user_forget_thePasswoed=input("Did you forget your password \n1-Yes \n2-NO:")
                  if if_user_forget_thePasswoed=="1":
                     print("You have to answer two saftey question that you made when you sign up.")
                     safety_question1=input("What is the best thing you like?:")
                     safety_question2=input("What is your nickname?:")
                     if not(safety_question1==stored_saftey_question1 and safety_question2==stored_saftey_question2):
                        print("You did not enterd the correct information!")
                        if not(safety_question1==stored_saftey_question1):
                           print("Your answer of the safety question one is wrong.")
                        else:
                           print("Your answer of the safety question two is wrong.")
                     else:
                        #chenge the password again
                        while True:
                           password=input("enter your new password :")
                           if len(password)<=7:
                              print("the passwor should be grater than 7 numbers")
                           else:
                              if not(search("[a-z]",password) and search("[A-Z]",password)):
                                 print("the password should contain cabital and small letters.")
                              else:
                                 if not(search("[0-9]",password)):
                                       print("the password should contain numbers.")
                                 else:
                                    if not(search("[!@#$%^&*]",password)):
                                       print("the password should contain symboles.")
                                    else:
                                       print("=="*10,"strong password !","=="*10)
                                       User_info.seek(0)
                                       new_password=User_info.readlines()
                                       new_password[2]=password+"\n"
                                       print("Password changed succefuly.")
                                       User_info.close()
                                       break
                     break
                  elif if_user_forget_thePasswoed=="2":
                     print("So try to enter your email and password again correctly.")
                  else:
                     print("Wrong choise! try again.")                   
            #cheching validation code
            else:
               print("Correct info! We are going to check if you are the real user.")
               check_code=""
               for i in range(5):
                  genaret_code=random.randint(1,9)
                  check_code+=str(genaret_code)
               current_time=datetime.datetime.now()
               send_time=current_time+datetime.timedelta(seconds=60)
               new_phone_num=""
               if "-" in stored_phone_number:
                  for i in stored_phone_number:
                     if i=="-":
                        continue
                     else:
                        new_phone_num+=i
               pywhatkit.sendwhatmsg(new_phone_num,f"your check code is {check_code}",send_time.hour,send_time.minute)
               print("We had sent check code to your phone number on WhatsApp,please open your WhatsApp and enter that code")
               send_code=input("Please enter the code you received:")
               if send_code==check_code:
                  print("\n"+'\033[92m'+("***"*15)+"Sign in succesful!"+("***"*15)+'\033[0m')
                  time.sleep(3)
                  os.system("cls")
                  print("\n"+'\033[92m'+("***"*15)+"\t Welcome to AL-hrazy Bank\t"+("***"*15)+'\033[0m')
                  break
               else:
                  print('\033[91m'+"\t\t\t\t\t\t\t\tFailed to sign in!"+'\033[0m')
                  try_again=input("Do you want to tryagain?\n1-Yes \n2-No:")
                  if try_again=="1":
                     continue
                  elif try_again=="2":
                     break
                  else:
                     print("Wrong choise!")
                     break
         break

      except:
        print("sorry you have error.")




have_account=input("Do you have account or no \n 1-yes! let me sign in:\n 2-no! creat account:")        
if have_account=="1":
   singe_in()
elif have_account=="2":
   sign_up()
else:
   print("Please try again there is no choice like that.")


  



  

