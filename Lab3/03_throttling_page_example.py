#Example of calling multiple webpages using throttling and timing
#without doing the request.  Note, this example does not make use of 
#elapsed time calculations.  To add, convert interval to a datetime
#object, then add the elapsed time calculation.  Note, this does do 
#an extra sleep interval.  For effeciency, you would need to weigh the cost 
#of an "if" statement to escape the last iteration vs. running the extra
#sleep command.
import time
import random

#parameter settings for easy changes.
lowint = 4
highint = 9

listosites = {'a.com', 'b.com', 'c.com', 'd.com'}

for site in listosites:
    interval = random.randint(lowint, highint) + random.random()
    print('Requesting Site:  ', site,'\n\tInterval:  ', interval, '\n\tTimeStamp: ', time.ctime())
    time.sleep(interval)
