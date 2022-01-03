import random
# how many rolls
# what range 
def dnd_dice(range_of_dice,number_of_rolls,rolls_list):
    roll = random.randint(0,range_of_dice)
    rolls_list.append(roll)
    print (roll)
    print (number_of_rolls)
    print (rolls_list)
    
range_of_dice = int(input("What range is your dice:"))
number_of_rolls = int(input("How many rolls:"))
rolls_list = []
dnd_dice(range_of_dice,number_of_rolls,rolls_list)
    