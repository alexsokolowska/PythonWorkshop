 #Write a stopwatch. It is supposed to start counting when you launch your program, say "Good job! Keep running!" every 60 seconds, and display an image.jpg when you stop it (and print the total elapsed time to your command line)

import os
import time

def save_your_score(score):
    if os.path.isfile("score.txt") == True:
        fh = open('score.txt', 'a')
    else: 
        fh = open('score.txt', 'w+')
    fh.write(str(score)+'\n')
    fh.close()
    
def print_all():
    fh = open('score.txt')
    data = fh.readlines()
    print "Your records:\n", data
    fh.close()
#or...    
    fh = open('score.txt')    
    for line in fh:
        print line
    fh.close()
    

raw_input("Hit enter to start. \n\n")
print "Here we go!\n"

start = time.time()

raw_input("Press enter to stop. ")
end = time.time() - start
print "You were running %d seconds." %(end)
save_your_score(end)
print_all()

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
logo = 'logo.png'
img = mpimg.imread(logo)
plt.imshow(img)
plt.show(block=False)
plt.pause(5)