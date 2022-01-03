import random
def dnd_dice(range_of_dice,number_of_rolls,rolls_list,i):
    if i != number_of_rolls:
        i += 1
        # randomly selects a number between 0 and wht user chose
        roll = random.randint(0,range_of_dice)
        rolls_list.append(roll)
        return (dnd_dice(range_of_dice,number_of_rolls,rolls_list,i))
    else:
        # for loop sums up all the rolls 
        sum = 0
        for e in rolls_list:
            e = int(e)
            sum = sum + e
        sum = str(sum)
        rolls_list = str(rolls_list)
        print ("Your Rolls: " + rolls_list)
        print ("Sum of rolls: " + sum)

# prompts user to input what is asked
range_of_dice = int(input("What range is your dice:"))
number_of_rolls = int(input("How many rolls:"))
rolls_list = []
i = 0
dnd_dice(range_of_dice,number_of_rolls,rolls_list,i)
    