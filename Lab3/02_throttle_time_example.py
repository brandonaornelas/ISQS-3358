#libraries needed for throttling.  
import random
import time

#This line will generate a random integer between 1,3.  Note that the function
#is inclusive of the top end number, unlike the range function you used in 
#loops during your python class.
y = random.randint(1,3)

#generates a random number between 0 and 1.  This is so we don't have exact
#second intervals.
x = random.random()
print(y)
print(x)
#this would be the interval done on this loop.
print(y+x)

#time.sleep stops python execution for a given time.  The parameter is the 
#number of seconds you would like to pause execution.
print('sleep now', time.ctime())
time.sleep(x+y)
print('wake up', time.ctime())