import time #used for loading aesthetics

print('==THE GREAT QUEST OF YUKERID==')
print()
input('Press Anything: ')
print()
for _ in range(15):   #prints code slowly to simulate a game...
    print("%loading%")
    time.sleep(0.05)

print() #spacing

save_files = ["Save File 1", "Save File 2", "Save File 3"] #values of save data
print("Select a save file:")
for i, file in enumerate(save_files):
    print(f"{i+1}. {file}")

selection = int(input("Enter the number of the save file: "))
print(f"Selected {save_files[selection-1]}")
print()
print('LOADING CUTSCENE...')
for _ in range(15):   #prints code slowly to simulate a game...
    print('%loading%')
    time.sleep(0.05)

print() #intro sequence...time.sleeps used for spacing of text

print('In a land long ago castles stood as fortresses and cities stood as beacons to early civilization...')
time.sleep(7)
print()
print('This land had just given up the pernicious idea of war and finally laid   down their swords and shields...')
time.sleep(7)
print()
print('The land was finally peaceful. The kingdom was reunited and Barclock was banished to the mountains of Raogdamith by the Starlinked Knights of Yukerid...')
time.sleep(7)
print()
print('These knights each had in their possession rocks that were mined from the mountains of Raogdamith and possessed necromancer-like power...')
time.sleep(7)
print()
print('But such power concentrated to the holds of an individual lead to the  mind-virus that took each of these Starlinked Knights and turned them into mindless zombies, constantly wanting more and more power...')
time.sleep(7)
print()
print('The land delved back into chaos...')
time.sleep(5)
print('... ... ...')
time.sleep(7)
print()
print('Each knight recruited their own army of different races to wage war and consume as much power as they could...')
time.sleep(7)
print()
print('Each army never rested. They rode all day with their undead armies atop of skeleton horses racing from village to village to plunder their resources, rape their women, and set the buildings ablaze...They are the merchants of chaos and death...')
time.sleep(7)
print()

for _ in range(15):   #prints code slowly to simulate a game...
    print('%loading%')
    time.sleep(0.05)

print()
print('YOU WAKE UP IN A DARK ROOM')
time.sleep(2)
print('THE DREAMS FROM LAST NIGHT FADE')
time.sleep(2)
print('YOU GO TO YOUR WATER BUCKET BENEATH THE WINDOW')
time.sleep(2)
print('A LITTLE BIT OF LIGHT IS CREEPING IN')
time.sleep(2)
print('YOU SPLASH YOUR FACE AND LOOK INTO THE REFLECTION')
time.sleep(2)
print('WHO ARE YOU?')
time.sleep(1)
print('...')
time.sleep(0.5)
print('...')
time.sleep(0.5)
print('...')
print()

name = input('\033[1mWhat is your name?: \033[0m')
print()

while True:
  print("""Choose your class:
  1. Mage
  2. Warrior
  3. Archer
  4. Assassin""")

  class_choice = input("Enter the number of the class you want to choose: ")
  if class_choice == "1":
    player_class = "Mage"
  elif class_choice == "2":
    player_class = "Warrior"
  elif class_choice == "3":
    player_class = "Archer"
  elif class_choice == "4":
    player_class = "Assassin"
    break
  else:
    print("Invalid choice. Please try again.")

print(f"You chose the {player_class} class.")