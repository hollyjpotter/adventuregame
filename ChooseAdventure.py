lives = 3

while lives > 0:
    print (' You have %d lives now! ' %(lives))
    answer1 = input(' You are Shrek and you are lost and do not know where your ' +
                    'swamp is. Do you want to go right or left? ')
    if (answer1 == "left"):
        answer2 = input(' You are safe. You may continue on. Right or left? ')
        if (answer2 == "right"):
            answer4 = input( ' Congrats you were not captured. Continue to the forest ' +
                            'or the lake? ')
        if answer4
    elif (answer1 == "right"):
        answer3 = input( ' You were captured by Lord Farquaad and are now in jail. ' +
                        ' You cannot continue on. ' )
        #Lives -= 1
        lives = lives -1
        continue
    else:
        print (' That is not an option sorry. ')
print (' You ran out of lives. ')
