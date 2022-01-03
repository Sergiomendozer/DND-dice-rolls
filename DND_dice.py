import random
# how many rolls
# what range 
def dnd_dice(range_of_dice,number_of_rolls):
    roll = random.randint(0,range_of_dice)
    print (roll)
    print (number_of_rolls)
    
range_of_dice = int(input("What range is your dice:"))
number_of_rolls = int(input("How many rolls:"))
rolls_list = []
dnd_dice(range_of_dice,number_of_rolls)
    