import random
# how many rolls
# what range 
def dnd_dice(range_of_dice,number_of_rolls,rolls_list,i):
    i += 1
    roll = random.randint(0,range_of_dice)
    rolls_list.append(roll)
    
    print (number_of_rolls)
    print (rolls_list)
    print (i)
    
range_of_dice = int(input("What range is your dice:"))
number_of_rolls = int(input("How many rolls:"))
rolls_list = []
i = 0
dnd_dice(range_of_dice,number_of_rolls,rolls_list,i)
    