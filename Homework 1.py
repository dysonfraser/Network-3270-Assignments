import matplotlib.pylab as plt
import numpy as np
import random
#Creates an array of the arrival rates
ar = [.2, .3, .4, .45, .5 , .55, .57, .58, .59]
def calc_average(arrival_rate):
#The predefined departure rate as well as arrays for the delay and average_delay
    departure_rate = .6
    delay = []
    average_delay = []
#Loop for each rate in the arrival_rate
    for rate in arrival_rate:
#For each new rate reset the queue to 0
        queue = 0
#This will measure 1 000 000 packages at each rate
        for i in range(10**6):
#Compare a random number generated from 0 to 1 against the arrival rate
#to see if you need to add an interger to the queue
            if random.random() < rate:
                queue += 1
#Compare a random number generated from 0 to 1 against the departure rate
#also checks if the queue is grater than zero as to not make the queue negative
            if random.random() < departure_rate and queue > 0:
                queue -= 1
#Add the queue value to an array for each I value
            delay.append(queue)
#Find the mean of the delay array and add it to the average_delay array.
        average_delay.append(np.mean(delay))

#Plot the graph of the arrival_rate and average_delay array
    plt.plot(arrival_rate,average_delay, label='Average Delay')
    plt.legend()
    plt.show()
calc_average(ar)