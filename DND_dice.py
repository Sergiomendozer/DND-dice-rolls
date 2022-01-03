import random
def dnd_dice(range_of_dice,number_of_rolls,rolls_list,i):
    if i != number_of_rolls:
        i += 1
        roll = random.randint(0,range_of_dice)
        rolls_list.append(roll)
        
        # print (number_of_rolls)
        # print (rolls_list)
        # print (i)
        return (dnd_dice(range_of_dice,number_of_rolls,rolls_list,i))
    else:
        sum = 0
        for e in rolls_list:
            e = int(e)
            sum = sum + e
        sum = str(sum)
        rolls_list = str(rolls_list)
        print ("Your Rolls: " + rolls_list)
        print ("Sum of rolls: " + sum)

range_of_dice = int(input("What range is your dice:"))
number_of_rolls = int(input("How many rolls:"))
rolls_list = []
i = 0
dnd_dice(range_of_dice,number_of_rolls,rolls_list,i)
    