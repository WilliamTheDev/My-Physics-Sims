import math

#Calculating the pressure inside a camber with a piston acting upon it
#By William

ATM = 101.325 #KPA
PistonMass = 35 #grams
PistonArea = 53 #cm^2
SpringForce = 50 #N

def PistonPressure():
    PS = SpringForce/(PistonArea*pow(10, -4))
    return PS

def PistonWP():
    PWP = ((PistonMass/100)*9.81)/(35*pow(10, -4))
    return PWP

CamberPressure = ((ATM*1000)+PistonPressure()+PistonWP())/1000 #Output KPA  
CamberPressureBAR = CamberPressure/100 # OutPut BAR
PressureDifference = (CamberPressure - ATM)/100 # OutPut BAR

print("CamberPressure: ", CamberPressureBAR, "BAR")
print("PressureDifference: ", PressureDifference, "BAR")
