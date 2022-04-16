import time
import sys
import random


active = True
elevatorFlag = True
suite2Flag = True
elevatorgift = 0
elevatorfood = 0
suite1entry = 0
suite2entry = 0
suite1food = 0
suite2food = 0
elevatorbox = {"food": "cookies", "weapon": "gun", "gift": "flowers"}
roombox1 = {
    "gift": "crown",
    "weapon": "knife",
    "food": "Water",
}
roombox2 = {
  "food": "Fruits", 
  "weapon": "sword", 
  "gift": "diamond"
  }
lobby = {
  "coins": 50, 
  "weapon": "gun"
  }
roombox3 = [
    "ball", "sunglasses", "book", "apple", "rubber duck", "dagger", "watch",
    "dice"
]
giftsbag = []
health = 100
coins = 0  # Collect coins and if you dont win a

print("You are in the cab on your way to the airport!")
print("When the driver happens to casually tell you that....")
print("The Queen is hiding at The Hotel Plaze!")
print("Only way to get her is to try your luck, collect all the gifts for her and then find her.\n")
time.sleep(3)
print("It made you think what's more fun? Boarding a boring flight or finding the Queen!!")
time.sleep(3)
print("....")
print("Driver wants to know where you wanna go!")
difficultchoice = input("Hotel or not? ")
if(difficultchoice == "Hotel"):
  print("LETS WIN THE QUEEN!\n")
  playerName = input("Please enter your name to begin the game: ")

  print(f"Please read the rules of the game.")
  time.sleep(1)
  print(f"The queen is hiding in one of the suites of the hotel.\n")
  time.sleep(1)
  print(f"And to be able to find her, \nyou have to get all the gifts for her - Flowers, \nThe Crown and a Diamond from the elevator, Suite 1 and Suite 2.\n"
  )
  time.sleep(1)
  print(f"Your health should be above 0% in order to move.\n")
  time.sleep(1)
  print(
      f"You will get some coins when you enter each room, \nwhich can be redeemed for health."
  )
  time.sleep(1)
  print(f"There are 3 suites, a lobby and an elevator.\n")
  time.sleep(1)
  print("There is one box in each room and elevator.\nYou can choose one item from the box. \n")
  print("If you get weapon, you die.\n")
  time.sleep(1)
  print("You can go to the elevator from the Lobby and \nsuites are accessible only through elevator or through one or the other suite.\n")
  print("Ohh Wait!! There is a catch.")
  time.sleep(1)
  print("Suite 3 is only accessible, once you cross Suite 1 and 2.")
  time.sleep(1)
  print(f"You win the game if you successfully reach and please the queen.")
  time.sleep(1)
  print("...")
  time.sleep(1)
  
else:
  print("Sad to see you go!")
  exit()

# Code for HealthMeter to boost health
def healthmeter():
    global health, coins
    if coins > 50:
        health += random.randint(20, 50)
        coins = coins - 50
        print(f"After boost, health: {health} and coins: {coins}.")
    else:
        print("Sorry you dont have enough coins to redeem.")
        sys.exit

# Code to begin the game.
def start_game():
    global health, coins, active
    print("Health: " + str(health))
    while active:
      choice = input("Please enter 'y' to continue and any other key to quit the game.")
      if (choice == 'y'):
        print(f"Welcome to Hotel Plaza, {playerName.title()}")
        print(f"Currently your health is at 100%, you have {len(giftsbag)} gifts for the queen and {coins} coins in your account.")
        choiceLobby = input("Please type 1 or 2 to enter your choice? ")
        if choiceLobby == '1':
          coins += int(lobby['coins'])
          print(f"Congratulations!! You get {coins} coins in your account. You can use them to improve your health.")
          time.sleep(2)
          print(f"You can now move to elevator to go to one of the suites to find the queen")
          nextStep = input( "Type in 1 to go to the elevator any other key to quit the game.")
          if (nextStep == '1'):
            elevator()
          else:
            print("Sorry to see you go!")
            sys.exit()
        elif choiceLobby == '2':
          print(f"Oh boy! You got the {lobby['weapon']}. You are dead.")
          sys.exit()
        else:
          print( f"Please enter number 1 or 2 to select one thing from the box.")
      else:
        print("Sorry to see you go!")
        sys.exit()

# Code for Elevator
def elevator():
  while elevatorFlag:
    global health, coins, elevatorgift, elevatorfood
    
    if (health < 20):
      print(f"Warning!! Health is at {health}. Please redeem your coins immediately to get the boost.")
      choiceHealth = input("Print 'y' to redeem your 50 coins. Any other key to quit the game.")
      if (choiceHealth == 'y'):
        healthmeter()
      else:
        print("You didnot redeem your coins for your health. You are now dead!")
        sys.exit()
    time.sleep(3)
    print(f"Hello {playerName.title()}, Location: Elevator")
    health = health - 15
    print(f"Health: {health}, Number of Gifts: {len(giftsbag)} and Coins: {coins}.")
    choice = input("Please type 1 or 2 or 3 to enter your choice? ")
    if choice == '1':
      health = health + 10
      print(f"You got the {elevatorbox['food']} to boost your health. Your health is now {health}")
      coins += random.randint(20, 70)
      elevatorfood = 1
      print(f"Coins = {coins}")
      print(f"You can now go to one of the suites to find the queen")
      
      suiteChoice1 = input( "Please input 1 for suite 1 and 2 for suite 2. ")
      if suiteChoice1 == '1':
        suite1()
      elif suiteChoice1 == '2':
        suite2()
      else:
        print( "This is not a valid choice in the elevator. You have to enter 1 or 2" )
    elif choice == '2':
      print(f"You got the {elevatorbox['weapon']}. You are dead.")
    elif choice == '3':
      print(f"Congratulations!! You got the {elevatorbox['gift']} for the Queen.You can now go to any suite.")
      giftsbag.append(elevatorbox['gift'])
      elevatorgift = 1
      health = health - 20
      suiteChoice = input("Please input 1 for suite 1 and 2 for suite 2. ")
      if suiteChoice == '1':
        suite1()
      elif suiteChoice == '2':
        suite2()
      else:
        print("This is not a valid choice in the elevator. ")
    else:
          print(f"Elevator: Please enter number 1 or 2 or 3 to select one thing from the box.")

# Code for Suite1
def suite1():
  global health, coins, suite1entry,suite1food
  time.sleep(3)
  print(f"Hello {playerName.title()}, Location: Suite 1")
  health = health - 15
  if (health < 20):
    print(f"Warning!! Health is at {health}. Please buy some food.")
    choiceHealth = input("Print 'y' to redeem your 50 coins. Any other key to quit the game.")
    if (choiceHealth == 'y'):
     healthmeter()
  coins += random.randint(20, 70)
  print(f"Health: {health}, Number of Gifts: {len(giftsbag)} and Coins: {coins}.")
  time.sleep(1)
  print("There is a box in front of you. ")
  print("Be careful! If you get a weapon, you will die and the queen will find another guy!!")

  choice = input("Please enter 1 or 2 or 3 to enter your choice? ")
  if choice == '1':
    giftsbag.append(roombox1['gift'])
    suite1entry = 1
    print(f"You got the {roombox1['gift']} for the Queen. Now you have {len(giftsbag)} gifts for the queen.")
    health = health - 20
    if (health < 20):
      print(f"Warning!! Health is at {health}. Please redeem your coins immediately to get the boost.")
      choiceHealth = input("Print 'y' to redeem your 50 coins. Any other key to quit the game.\n")
      if (choiceHealth == 'y'):
        healthmeter()
    
    if (len(giftsbag) == 3):
      choiceSuite3 = input( "You are now qualified for suite 3.Please enter y to continue, any other key to quit the game. \n")
      if (choiceSuite3 == 'y'):
        suite3()
      else:
        print("Sorry to see you go.")
        letsRestart()
    else:
      print("You can now move suite 2.")
      chooseSuite2 = input("Please enter 'y' to continue, any other key to quit the game.\n")
      if (chooseSuite2 == 'y'):
        suite2()
      else:
        sys.exit()

  elif choice == '2':
    print(f"You got the {roombox1['weapon']}. You are dead.")
    sys.exit
  elif choice == '3':
    while suite1food != 0:
      print("This choice is not available at the moment.")
      choice = input("Please enter 1 or 2 or 3 to enter your choice? ")

    health += 10
    print(f"You got the {roombox1['food']} to boost your health. Your health is now {health}")
    suite1food = 1

    print("You can now move suite 2.")
    chooseSuite2 = input("Please enter 'y' to continue, any other key to quit the game")
    if (chooseSuite2 == 'y'):
      suite2()
    else:
      sys.exit()
  else:
    print("Please enter number 1 or 2 or 3 to select one thing from the box.")

# Code for Suite2
def suite2():
  global health, coins, elevatorgift, suite2entry,suite2food
  time.sleep(3)
  print(f"Hello {playerName.title()}, You are now entering Suite 2.")
  health = health - 15
  if (health < 20):
    print(f"Warning!! Health is at {health}. Please redeem your coins immediately to get the boost.")
    time.sleep(1)
    choiceHealth = input("Print 'y' to redeem 50 coins. Any other key to quit the game.")
    if (choiceHealth == 'y'):
      healthmeter()
    else:
      sys.exit()
  
  coins += random.randint(10, 50)
  print(f"Health: {health}, Number of Gifts: {len(giftsbag)} and Coins: {coins}.")
  time.sleep(3)
  print(f"You have to chose an item from the box!")
  print("Be careful! If you get a weapon, you will die and queen wont wait till eternity.")
  time.sleep(1)
  choice = input("Please enter 1 or 2 or 3 to choose an item from the box or any other key to quit the game.")
  if choice == '1':
    if(suite2food == 0):
      while suite2food != 0:
        print("This choice is not available at the moment.")
        choice = input("Please enter 1 or 2 or 3 to enter your choice? ")
      health += 10
      print(f"You got the {roombox2['food']} and now your health is {health}%")
      suite2food = 1
    else:
      print("This choice is not available at the moment in Suite1.")
  elif choice == '2':
    print(f"You got the {roombox2['weapon']}. You are dead.")
    sys.exit
  elif choice == '3':
    giftsbag.append(roombox2['gift'])
    print(f"Bravo!!! You got the {roombox2['gift']} for the Queen.")
    suite2entry = 1
    health = health - 20
    if (health < 20):
      print(f"Warning!! Health is at {health}. Please redeem your coins immediately to get the boost.")
      choiceHealth = input("Print 'y' to redeem your 50 coins. Any other key to quit the game.")
      if (choiceHealth == 'y'):
        healthmeter()
      
    if (len(giftsbag) == 3):
      choiceSuite3 = input("You are now qualified for suite 3.Please enter y to continue: \n")
      if (choiceSuite3 == 'y'):
        suite3()
    else:
      print("Queen's very demanding. You will only get her if you have 3 gifts. Please go back and find out where are the other gifts.")
      yourchoice = input("Where do you wanna go first? Press 1 for elevator and 2 for suite 1.")
      while yourchoice:
        if(yourchoice == '1' and  elevatorgift == 0):
          elevator()
        elif (yourchoice == '2' and suite1entry == 0):
          suite1()
        elif(yourchoice == '1' and  elevatorgift == 1):
          print("You already have gift from the Elevator. Please check Suite 1")
          suite1()
        elif(yourchoice == '2' and suite1entry == 1):
          print("You already have gift from there. Please check the elevator.")
          elevator()
  else:
    print("Sorry to see you go!!")
    letsRestart()

# Code for Suite3
def suite3():
  global health, coins
  time.sleep(3)
  print(f"Hello {playerName.title()}, You are now entering suite 3.")
  print("But, before you jump into excitement...There is one last hurdle..!")
  print("You can still die if you get a weapon..so be careful.")
  choice = input("Please enter a number between 1 to 8 to select an item from the trunk.")
  boxitemnumber = random.randint(1, 7)
  print(boxitemnumber)
  boxitem = roombox3[boxitemnumber].lower()
  print(boxitem)
  if (boxitem != "dagger" and int(choice) != 6):
    print("Woohoo!! You crossed the last hurdle to reach the queen.")
    print("Please give your bag full of gifts to the queen")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("Queen is very impressed by your efforts: specially the gifts.")
    print("AAAANNNNNNDDDDDD......YOU WIN!!")
    letsRestart()    
  else:
    print("Aagh! Hard Luck. You got a Dagger!! You are dead.")
    exit()
        
#Restart the game: 
def letsRestart():
  global health, coins, active, elevatorFlag,suite2Flag,elevatorgift,suite1entry,suite2entry
  restart = input("Do you want to restart the game? y to yes, any other key to quit the game? \n")
  if(restart == 'y'):
    active = True
    elevatorFlag = True
    suite2Flag = True
    elevatorgift = False
    suite1entry = 0
    suite2entry = 0
    giftsbag.clear()
    health = 100
    coins = 0
    start_game()
  else:
    exit()

start_game()