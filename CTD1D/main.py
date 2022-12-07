import random #rya
import time

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
   if account_balance <= 0:
       print("You Lost :( try again!")
       exit()
   elif account_balance >= 1000:
       print("YAY! you saved $1000, you're now a financially responsible citizen!")
       exit()

def game():

 print("You now have an allowance of $200! Let's start the game")

question1 = input("You wake up and it's a nice windy morning, \n (1)would you like to sleep in and take grab,\n (2) or wake up and take the school bus\n Type in 1 OR 2")
if question1 == "1":
   print("you spend $15 on the grab")
   account_balance= account_balance - 15
   print('Your account balance is now $' + str(account_balance))
elif question1 == "2":
   print("congrats you saved $15")
   time.sleep(2)
   print('Your account balance is now $' + str(account_balance))
else:
   print("Invalid Input, Run again\n")
   exit()
time.sleep(2)
question2 = input("Your mother askes you to pack your lunch and take it to school or askes you to use your allowance to buy food, \n (1)make yourself a peanut butter sandwhich,\n (2) or spend money on yummy canteen food\n Type in 1 OR 2")
if question1 == "1":
   print("Congrats! you saved $4")
   print('Your account balance is now $' + str(account_balance))
elif question1 == "2":
   print("you spend $4 on Nasi Lemak")
   time.sleep(2)
   account_balance= account_balance-4
   print('Your account balance is now $' + str(account_balance))
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
   print("Individual stocks are lika a gamble. You never know which company will increase flourish and which company will fail. The company you chose to invest in failed. You have lost your $100")
   print('Your account balance is now $' + str(account_balance))
elif question3 == "2":
   answer1 = input("The market is down, would you like to remove all of your money from the fund? (y = yes, n = no )")
   if answer1 == "y":
    print("\nETFs might not always produce a profit in the short-run, and it might even incur losses, it is important to be patient and wait till the ,market reaches a profit before you take your money out!")
    account_balance= account_balance/1.5
    print('Your account balance is now $' + str(account_balance))
   elif answer1 == "n":
    print("ETFs might not always produce a profit in the short-run, and it might even incur losses, it is important to be patient and wait till the ,market reaches a profit before you take your money out! Good job on being patient!")
    account_balance = account_balance*2
    print('Your account balance is now $' + str(account_balance))
   else:
    print("Invalid Input, Try again\n")
    game()
elif question3 == "3":
   time.sleep(2)
   print('Your account balance is now $' + str(account_balance))
else:
   print("Invalid Input, Run again\n")
   exit()
import turtle #joel
account_balance = 200
question4 = input("Your exams just finished and your friends want to go to a chalet together, \n (1)would you like to join them?,\n (2) or miss out on the fun and stay at home?\n Type in 1 OR 2")
if question4 == "1":
   answer3 = input("You agreed to go for the chalet. Your friends are splitting the costs evenly amongst everyone. \n Would you like to \n (1) Pay a part of the cost for the chalet - $20 \n (2) Pay for the food and drinks -$15 ")
   if answer3 == '1':
       print('You have decided to contribute by paying for a part of the chalet cost')
       time.sleep(2)
       account_balance = account_balance-20
       print('Your account balance is now $'+ str(account_balance))
   elif answer3 == '2':
       print('You have decided to contribute by paying for the food and drinks')
       account_balance = account_balance -15
       print('Your account balance is now $'+ str(account_balance))
   else:
       print("Invalid Input, Run again\n")
       exit()
elif question3 == "2":
    print('You have decided to save money and stay at home.')
else:
    print("Invalid Input, Run again\n")
    exit()
question5 = input("Since the exams are over and its holiday season,  \n (1)Do you want to find a part time job?,\n (2) Or have fun during the holidays?\n Type in 1 OR 2")
if question5 == "1":
   answer4 = input("You have agreed to find a part time job \n After searching for a while you have found 2 jobs: \n (1) Bubble tea part time job ( More relaxed ) - $8/hr \n (2) Banquet server job ( More hectic )- $10/hr ")
   if answer4 == '1':
       print('You have decided to work at a bubble tea shop for one month!')
       workinghours= input('How often will you work in the one month? Please enter your total working hours for the month')
       pay= 8*float(workinghours)
       time.sleep(2)
       account_balance = account_balance+(pay)
       print('Your account balance is now $'+ str(account_balance))
       print('Since you have read up more on stocks and experienced a little from stocks,')
       answer5 = input('Do you want to put the money you earned from this job into stocks? \n (1) Invest your pay \n (2) Keep your pay in your account balance')
       if answer5 == '1':
           print('you have decided to invest your pay consisting of ' +str(pay) +' into stocks')
           p= random.randint(1, 10)
           if p<5:
               print('Unfortunately, the stocks that you have invested in did not perform well and you have lost 2 times the amount that you put in')
               win = turtle.Screen()
               win.setup(width=800, height=600)
               win.bgpic("unknown.gif")
               t = turtle.Turtle()
               t.shape('classic')  # <---
               t.circle(60)
               turtle.bye()
               account_balance= account_balance - (2*pay)
               print('Your account balance is now $'+ str(account_balance))
           else:
               print('Congratulations, you have made a smart choice and you have earned $300 from stocks')
               account_balance=account_balance + 300
               time.sleep(1)
               print('Your account balance is now $'+ str(account_balance))
   elif answer4 == '2':
       print('You decided to work for the banquet job for one month! ')
       workinghours = print('You have been assigned to work 6 days a week, each day 5 hours')
       pay= 10*150
       account_balance = account_balance+ float(pay)
       print('Your account balance is now $'+ str(account_balance))
       print('Since you have read up more on stocks and experienced a little from stocks,')
       answer6 = input('Do you want to put the money you earned from this job into stocks? \n (1) Invest your pay \n (2) Keep your pay in your account balance')
       if answer6 == '1':
           print('you have decided to invest your pay consisting of ' + str(pay) + 'into stocks')
           p = random.randint(1, 10)
           if p < 5:
               print('Unfortunately, the stocks that you have invested in did not perform well and you have lost 2 times the amount that you put in')
               account_balance = account_balance - (2 * pay)
               print('Your account balance is now $'+ str(account_balance))
           else:
               print('Congratulations, you have made a smart choice and you have earned $300 from stocks')
               account_balance = account_balance + 300
               print('Your account balance is now $'+ str(account_balance))
   else:
       print("Invalid Input, Run again\n")
       exit()
else:
    print('You have decided to relax during the holidays. Your account balance remains the same.')
question10 = input("the fixed deposit rate in singapore have increased to 3.8% do you want to put some money into bank account? \n (1)Yes \n (2)No")
if question10 == "1":
    principal = float(input('enter the amount you want to deposit from $100-$1000:'))
    account_balance = account_balance - principal
    duration = float(input('enter how many months do you wish to save for ?'))
    deposit = round((principal * 3.8 * duration) / 100, 2)
    answer10a = input("next week is you birthday, do you want to hold a party? \n (1)yes, you will need to draw from your fixed deposit account, \n (2)no")
    if answer10a == '1':
        answer10b = input("where do you want to hold your birthday party? \n (1)home, \n (2)chalet")
        if answer10b == "1":
            print('the birthday party cost $100')
            time.sleep(2)
            account_balance = account_balance - 100 + 300
            print('Your account balance is now $' + str(account_balance))
            answer10c = input('your grandma came over to your birthday party and gave you $250 in cash.\n Do you want to \n (1)spent it with your friends \n (2)save the money:')
            if answer10c == '1':
                    print('you went out with friends for a meal and a movie you spent all the $250 given')
                    time.sleep(2)
                    account_balance = account_balance
                    print('Your account balance is now $' + str(account_balance))
            elif answer10c == '2':
                    print('well done! you now have an additional $250 in your account')
                    time.sleep(2)
                    account_balance = account_balance + 250
                    print('Your account balance is now $' + str(account_balance))
            else:
                    print("Invalid Input, Run again\n")
                    exit()

        elif answer10b == '2':
            print('the birthday party cost $500')
            time.sleep(2)
            account_balance = account_balance - 500
            print('Your account balance is now $' + str(account_balance))

        else:
            print("Invalid Input, Run again\n")
            exit()

    elif answer10a == '2':
        print('good choice! {} have been credited to your account'.format(deposit))
        time.sleep(2)
        account_balance = account_balance + deposit + principal
        print('Your account balance is now $' + str(account_balance))
    else:
        print("Invalid Input, Run again\n")
        exit()

elif question10 == '2':
    account_balance = account_balance
    print('Your account balance is now $' + str(account_balance))

else:
    print("Invalid Input, Run again\n")
    exit()

question11 = input('you came across a luckydraw and the entry fee is $300 \n 1st price $1000 \n 2nd price $500 \n 3rd price $100 .\nDo you want to give it a try? \n (1)yes \n (2)no')
if question11 == '1':
    account_balance = account_balance - 300
    LD1 = random.randint(1000, 9999)
    LD2 = random.randint(1000, 9999)
    LD3 = random.randint(1000, 9999)
    answer11 = int(input('please enter 3 random 4 digit number \n first number:'))
    answer12 = int(input('second number:'))
    answer13 = int(input('third number:'))
    list_of_answers = [answer11, answer12, answer13]
    if LD1 in list_of_answers:
        print('congratulations, you have won 1st price $1000!')
        time.sleep(2)
        account_balance = account_balance + 1000
        print('Your account balance is now $' + str(account_balance))

    elif LD2 in list_of_answers:
        print('congratulations, you have won 2nd price $500!')
        time.sleep(2)
        account_balance = account_balance + 500
        print('Your account balance is now $' + str(account_balance))

    elif LD3 in list_of_answers:
        print('congratulations, you have won 3rd price $100!')
        time.sleep(2)
        account_balance = account_balance + 100
        print('Your account balance is now $' + str(account_balance))

    else:
        print('opps bad luck you won nothing HAHA')
        time.sleep(2)
        account_balance = account_balance
        print('Your account balance is now $' + str(account_balance))
elif question11 == '2':
        account_balance = account_balance
        print('Your account balance is now $' + str(account_balance))

else:
        print("Invalid Input, Run again\n")
        exit()
question6=input("During your school holidays, your friends invite you for a overseas trip to Japan ,\n (1) Join the trip Japan, \n (2) Skip the trip and instead have a staycaytion in Singapore? \n Type 1 OR 2 ")
if question6 == "1":
    answer8=input(" You agreed to go for the Japan trip. Would you like to \n (1) Share a BIGGER hotel room with your friends? - $100 , \n (2) Have a SMALLER hotel room to yourself? - $ 250 \n Type 1 OR 2 ")
    if answer8 == '1':
        print("You agreed to share a room with your friends")
        time.sleep(2)
        account_balance=account_balance-100
        print("Your account balance is now $"+ str(account_balance))
    elif answer8 == '2':
        print("You have decided to live comfortably in your own hotel room")
        time.sleep(2)
        account_balance=account_balance-250
        print("Your account balance is now $"+ str(account_balance))
    else:
        print("Invalid Input, Run again\n")
        exit()
elif question6 == "2":
    print("You decided to save some money and have a staycay in Singapore.")
    account_balance=account_balance- 50
    print("Your account balance is now $"+ str(account_balance))
    answer9=input("To travel around Singapore while on your staycay would you \n (1) Take public transport? - $3, \n (2) Call a Grab car to drive you around? - $25 \n Type 1 OR 2 ")
    if answer9 == '1':
        print("You have decided to save some money and take public transport")
        time.sleep(2)
        account_balance=account_balance- 3
        print("Your account balance is now $"+ str(account_balance))
    elif answer9 == '2':
        print("You have decided spend more money to travel with ease in a Grab car")
        time.sleep(2)
        account_balance=account_balance- 25
        print("Your account balance is now $"+ str(account_balance))
else:
    print("Invalid Input, Run again\n")
    exit()
question7=input("Your friends are hosting a Christmas party and are having a pot luck.Do you \n (1) Buy a log cake from a cake shop. , \n (2) Buy ingredients and bake our own log cake? \n Type 1 OR 2 ")
if question7 == "1":
    answer10=input(" You chose to buy a log cake for the Christmas party. Where do you want to buy the log cake from? \n (1) A specially cutomised log cake from The Cake Shop. - $75 , \n (2) A standard log cake from BreadTalk - $40 \n Type 1 OR 2  ")
    if answer10 == '1':
        print("You chose to spend a little more money to buy a specially made cake from The Cake Shop.")
        time.sleep(2)
        account_balance=account_balance-75
        print("Your account balance is now $"+ str(account_balance))
    elif answer10 == '2':
        print("You chose to all out on an unnecessarily expensive log cake.")
        time.sleep(2)
        account_balance=account_balance-40
        print("Your account balance is now $"+ str(account_balance))
    else:
        print("Invalid Input, Run again\n")
        exit()
elif question7 == "2":
    print("You have decided to save some money and bake your own log cake from scratch")
    time.sleep(2)
    account_balance=account_balance-20
    print("Your account balance is now $"+ str(account_balance))
else:
    print("Invalid Input, Run again\n")
    exit()
question8=input(" Apple just released the latest Iphone and everyone is scrambling to get it. \n (1) Do you buy a new phone to keep up with the trends? , \n (2) Use the phone that you currently have that is working perfectly fine?  \n Type 1 OR 2 ")
if question8 == "1":
    print("You chose to buy a new phone.")
    time.sleep(2)
    account_balance=account_balance-200
    print("Your account balance is now $"+ str(account_balance))
    answer10=input(" You chose to buy the new Iphone. But unfortunately on the way to school you dropped it and the tempered glass screen protector cracked. Do you \n (1) Get a new screen protector  , \n (2) Continue to use the phone with the cracked screen protector \n Type 1 OR 2  ")
    if answer10 == '1':
        print("You chose to get your screen protector replaced.")
        time.sleep(2)
        account_balance=account_balance-30
        print("Your account balance is now $"+ str(account_balance))
    elif answer10 == '2':
        print("You chose to continue using your phone with the cracked screen.")
        time.sleep(2)
        print("Your account balance is now $"+ str(account_balance))
    else:
        print("Invalid Input, Run again\n")
        exit()
elif question8 == "2":
    print("You chose to use your current phone and save money rather than spend it on a new phone that you did not need.")
    time.sleep(2)
    print("Your account balance is now $"+ str(account_balance))
else:
    print("Invalid Input, Run again\n")
    exit()
play_loop()
game()
