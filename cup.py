import matplotlib.pyplot as plt
import math

"""
Problem statement: Given a glass of water with some volume of water in it, what is the maximum angle that we can tilt it so that it doesn't spill out?

We solve a similar problem: Given a full glass of water, if we hold it at an angle theta, how much liquid is left?

Given this, we can then interpolate an answer for the first problem.

Assume that a glass has radius 1 and height h.

Model this as a cylinder:
(x-1)^2 + y^2 = 1, 0<=z<=h

Let the tilt be a plane, e.g. z = x, which cuts the glass at a 45 deg angle from the mouth.
For generality we call this z = mx, where m is the gradient of the line, from which the angle can be calculated, as arctan(m)

To find the vol of water left, we need to find the x coordinate that the plane intersects the circular base, which is (x-1)^2 + y^2 = 1, z=h;

This is solved as h = mx, so x = h/m, notice that there can be a non-intersection with the base, if this value of x does not lie in [0,2].

The volume of air is thus total volume - volume under slope - volume under flat base.

Total volume: PI*h
Volume under slope: \int_0 ^{\min(2,h/m)} \int_{-\sqrt{1-(x-1)^2}} ^ {\sqrt{1-(x-1)^2}}  mx dy dx
Volume under flat base: \int_{\min(2,h/m)}^2 \int_{-\sqrt{1-(x-1)^2}} ^ {\sqrt{1-(x-1)^2}} h dy dx

which Wolfram evaluates to:
Volume under slope: \frac{m}{3}\sqrt{-(x-2)x}(2x^2-x-3)-2m\arcsin{\sqrt{1-x/2}} + C
Volume under flat base: h(x-1)\sqrt{-(x-2)x} - 2h\arcsin{\sqrt{1-x/2}} + C

We evaluate these for cylinders of height 1 to 10, for 1 to 89 degrees of the base from the horizontal
"""

heightList = list(range(1,11))

def slopeVolume(m,x):
    return (m/3)*math.sqrt(-(x-2)*(x))*(2*x*x-x-3) - 2*m*math.asin(math.sqrt(1-x/2))

def flatVolume(h,x):
    return h*(x-1)*math.sqrt(-(x-2)*x)-2*h*math.asin(math.sqrt(1-x/2))

def getPlaneGradient(angle):
    return math.tan(math.radians(angle))
                    
def evaluateForAngle(angle):
    m = math.tan(math.radians(angle))
    print(m)
    
def getAirVolume(h,m):
    slopeVol = slopeVolume(m,min(2,h/m))-slopeVolume(m,0)
    flatVol = flatVolume(h,2)-flatVolume(h,min(2,h/m))
    return slopeVol + flatVol

def getAirVolumeClosedFormula(h,m):
    k = min(2,h/m)
    slopeVol = 2*m*((1/6)*math.sqrt(-(k-2)*k)*(k+1)*(2*k-3)+math.asin(math.sqrt(k/2)))
    flatVol = 2*h*math.asin(math.sqrt(1-k/2))-h*(k-1)*math.sqrt(-(k-2)*k)
    return slopeVol + flatVol

def getWaterVolume(h,angle):
    totalVolume = math.pi*h
    m = getPlaneGradient(angle)
    airVolume = getAirVolumeClosedFormula(h,m)
    return totalVolume-airVolume

def getPlot():
    plt.ylabel("Max volume of water that the cup can contain")
    plt.xlabel("Angle of base from horizontal (in degrees)")
    x = list(range(1,90))
    for height in heightList:
        y = []
        for i in range(1,90):
            y.append(getWaterVolume(height,i))
        plt.plot(x,y, label=f"Height: {height}")
    plt.legend()
    plt.show()

getPlot()


