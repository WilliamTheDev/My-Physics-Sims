import math
from math import sqrt
from math import sin
from math import cos

# This program calculates the motion of an projectile.
# Equations:

# Non-elevated position (Initial Height h = 0)
# - VelocityX = Inital velocity * cos(Angle) | Horizontal Velocity Component
# - VelocityY = Inital Velocity * sin(Angle) | Vertical Velocity Component
# - Time = 2 x VelocityY / Gravity | Time Of flight
# - Range = 2 x VelocityX * VelocityY / Gravity | Projectile range
# - MaxHeight = VelocityY² / (2 * Gravity) | Maximum Height

# Elevated position (Initial Height h > 0)
# - VelocityX = Inital Velocity * cos(Angle) | Horizontal Velocity Component
# - VelocityY = Inital Velocity * sin(Angle) | Vertical Velocity Component
# - Time = [VelocityY + √(VelocityY² + 2 x gravity x height)] / gravity) | Time Of Flight
# - Range = VelocityX x [VelocityY + √(VelocityY² + 2 x gravity x height)] / gravity | Projectile range
# - MaxHeight = Height + VelocityY²/(2 x gravity)

# Inital Parameters
InitalVelocity = 0 #Meters per second
InitalAngle = 0 #Degrees 

# Simulation Parameters 
Gravity = 9.81 # Meters per second 
Height = 0 #Meters

def VelocityX():
    VelocityX = InitalVelocity * cos(InitalAngle)
    return VelocityX

def VelocityY(): 
    VelocityY = InitalVelocity * sin(InitalAngle)
    return VelocityY

def MagniteVelcoity(): 
    mv = round(sqrt(pow(VelocityX(), 2) + pow(VelocityY(), 2)), 2)
    return mv

def nonelevated():
    Time = 2 * VelocityY() / Gravity
    Range = 2 * VelocityX() * VelocityX() / Gravity
    MaxHeight = (VelocityY() * VelocityY()) / (2* Gravity)
    return Time, Range, MaxHeight

def elevated():
    Time = (VelocityY() + sqrt(((VelocityY() * VelocityY()) + 2 * Gravity * Height))) / Gravity
    Range = VelocityX() * (VelocityY() + sqrt((VelocityY()+VelocityY()) + 2 * Gravity * Height)) / Gravity
    MaxHeight = Height + (VelocityY() * VelocityY()) / (2 * Gravity)
    return Time, Range, MaxHeight


if Height == 0:
    data = nonelevated()
    print("Magnite Velcoity:  " + str(MagniteVelcoity()) + " Meter per second")
    print("Fight Time: " + str(data[0]) + " seconds")
    print("Range: " + str(data[1]) + " Meters")
    print("MaxHeight: " + str(data[2]) + " Meters")

if Height > 0:
    data = elevated()
    print("Magnite Velcoity:" + str(MagniteVelcoity()) + " Meter per second")
    print("Fight Time: " + str(data[0]) + " Seconds")
    print("Range: " + str(data[1]) + " Meters")
    print("MaxHeight: " + str(data[2]) + " Meters")








