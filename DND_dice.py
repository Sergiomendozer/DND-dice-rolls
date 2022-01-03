import random
# how many rolls
# what range 
def dnd_dice(range_of_dice):
    roll = random.randint(0,range_of_dice)
    print (roll)
    
range_of_dice = int(input("What range is your dice:"))
dnd_dice(range_of_dice)
    