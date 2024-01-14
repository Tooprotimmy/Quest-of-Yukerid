import time

print("==YUKERID CHARACTER SELECTION==")

name = input("What is your name, traveler?: ")
print(name,", welcome to the world of Yukerid...")
print()
print("Let us go forth and create your character...")

for _ in range(7):
    print("%loading%")
    time.sleep(0.5)
print()
print("==CHARACTER CREATION==")
print()
time.sleep(2)

print("Every adventurer needs a sword...let me introduce you to a couple:")
print()
time.sleep(2)
print("==SWORDS==")
time.sleep(3)
print(
    "For our first sword let me introduce you to Excalibur, a long broad sword once weilded by the king of the last kingdom of Men. Excalibur is jeweled with a golden hilt and mixed with a resin of gems that is mixed with the steel giving a hybrid stone look. It is said that the sword was forged by the finest smiths from Raogdamith...")
print()
time.sleep(3)
excalibur = input("Do you want to equip Excalibur? (yes/no): ")
if excalibur == "yes": 
                  print("A fantastic sword! Excalibur has been added to your inventory. Moving on!")
elif excalibur == "no":
    print("Let me introduce you to another sword...Diagola, a long sword lost in Tajumi river that was once wielded by a massive giant. The sword is made of obsidian and strength is it's greatest attribute... ")
    diagola = input("Do you want to equip Diagola? (yes/no): ")
    if diagola == "yes":
      print("Diagola has been added to your inventory! Moving on!")
    elif diagola == "no":
      print("How about another one. Let me introduce you to the sword of the gods, Mayauke, a sword of sorcerer and magic.")
      mayauke = input("Do you want to equip Mayauke? (yes/no): ")
      if mayauke == "yes":
        print("Mayauke has been added to your inventory! Moving on!")
      elif mayauke == "no":
        print("Well I have no more swords for you...guess you will have to just go empty handed!")
        time.sleep(3)

else:
  print("You must pick a sword, dummy!")


print("Let's choose your hair color!!")
