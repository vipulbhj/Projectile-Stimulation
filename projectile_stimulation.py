"""
This is a simple Projectile stimulation , 
with angle a and initial velocity u.
Tested with time interval of 1 sec.
Adding functionality of custom time frame available to the users and,
making integers to floats.
Tested.
Ploted all the values obtained , using matplotlib.pyplot
Updated to take initial coordinates by the user.
"""

from math import sin,cos,pi as PI
import matplotlib.pyplot as plt


# Converts degree to radian format
def degToRad(deg):
    return (PI * deg) / 180

# Output's the total number of iteration required to calculate the trajectory.
def flightFrames(yVel,timeFrameSize):
    t = yVel / 9.8
    # 0.01 second mean that 1 second is divided into 100 parts 
    # So to get all the intervals , we can multiple the -1 power of the framesize to number of seconds.
    return 2 * t * (1 / timeFrameSize)


def main():
    # Initialize the starting point
    x = input("Enter initial value of x co-ordinate or press enter to use 0: ")
    x = 0 if x == '' else float(x)
    y = input("Enter initial value of y co-ordinate or press enter to use 0: ")
    y = 0 if y == '' else float(y)

    # Declaring a list for coordinate Storage
    # Initializing with (0,0)
    coordinate = [(x,y)]
    
    # prompt the user
    u = float(input("Enter the initial velocity:  "))
    a = float(input("Enter the initial angle in degree's:  "))
    timeFrameSize = float(input("Enter the interval you want for time: "))
    
    # Calculating velocity components
    uX = u * cos(degToRad(a))
    uY = u * sin(degToRad(a))

    # Calculating total flight time.
    T = round(flightFrames(uY,timeFrameSize))

    # Calculating all the coordinates of the motion state.1
    for i in range(T):
        x += uX * timeFrameSize
        y += uY * timeFrameSize - (9.8 / 2 ) * pow(timeFrameSize,2)
        coordinate.append((round(x,2),round(y,2)))
        uY -= 9.8 * timeFrameSize

    # Drawing projectile using matplotlib.
    x , y = zip(*coordinate)
    plt.scatter(x,y)
    plt.show()


if __name__ == '__main__':
    main()