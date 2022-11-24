import random #rya
import time
import urllib
print ("Welcome to Learn2Save " )
name = input("what's your name :):")
print ("welcome " + name+ " to this game, where we teach you all the important basics of financial literacy. Your goal is to save $1000!")
time.sleep(2)
account_balance = 200
print("this is your account balance")
time.sleep(2)
print(account_balance)
time.sleep(2)

def play_loop():
   if account_balance == 0:
       game()
   elif account_balance <= 1000:
       print("YAY! you saved $1000, you're now a financially responsible citizen!")
       exit()

def game():

 print("You now have an allowance of $200! Let's start the game")

question1 = input("You wake up and it's a nice windy morning, \n (1)would you like to sleep in and take grab,\n (2) or wake up and take the school bus\n Type in 1 OR 2")
if question1 == "1":
   print("you spend $15 on the grab")
   account_balance= account_balance - 15
   print(account_balance)
elif question1 == "2":
   print("congrats you saved $15")
   time.sleep(2)
   print(account_balance)
else:
   print("Invalid Input, Run again\n")
   exit()
time.sleep(2)
question2 = input("Your mother askes you to pack your lunch and take it to school or askes you to use your allowance to buy food, \n (1)make yourself a peanut butter sandwhich,\n (2) or spend money on yummy canteen food\n Type in 1 OR 2")
if question1 == "1":
   print("Congrats! you saved $4")
   print(account_balance)
elif question1 == "2":
   print("you spend $4 on Nasi Lemak")
   time.sleep(2)
   account_balance= account_balance-4
   print(account_balance)
else:
   print("Invalid Input, Run again\n")
   exit()
time.sleep(2)
print("Your friend tells you that to get more money fast, you should invest in stocks.\n Your teacher tells you that the best way to increase income slowly but steadily is through an ETF fund, you go home to read up more about it in the links below" )
print("https://www.investopedia.com/etfs-4427784")
print("https://www.marketwatch.com/story/financial-face-off-during-this-volatile-stock-market-is-it-better-to-buy-individual-stocks-or-invest-in-an-etf-11666010483#:~:text=Picking%20individual%20stocks%20lets%20investors,%2C%20bonds%2C%20commodities%2C%20currency.")
time.sleep(5)
question3= input("Do you: \n (1) Invest $100 an indivual stock of a company \n OR \n (2)invest $200 into an ETF \n OR \n (3) just leave your money in your savings account \n type in1/2/3")
time.sleep(2)
if question3 == "1":
   account_balance= account_balance - 100
   print("Individual stocks are lika a gamble. You never know which company will increase florish and which company will fail. The company you chose to invest in failed. You have lost your $100")
   print(account_balance)
elif question3 == "2":
   answer1 = input("The market is down, would you like to remove all of your money from thr fund? (y = yes, n = no )")
   if answer1 == "y":
    print("\nETFs might not always produce a profit in the short-run, and it might even incur losses, it is important to be patient and wait till the ,market reaches a profit before you take your money out!")
    account_balance= account_balance/1.5
    print(account_balance)
   elif answer1 == "n":
    print("ETFs might not always produce a profit in the short-run, and it might even incur losses, it is important to be patient and wait till the ,market reaches a profit before you take your money out! Good job on being patient!")
    account_balance = account_balance*2
    print(account_balance)
   else:
    print("Invalid Input, Try again\n")
    game()
elif question3 == "3":
   time.sleep(2)
   print(account_balance)
else:
   print("Invalid Input, Run again\n")
   exit()
